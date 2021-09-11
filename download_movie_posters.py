## Importing Necessary Modules
import requests # to get image from the web
import shutil # to save it locally
import pandas as pd # to import csv file
import os
from pandasql import sqldf


df_movies = pd.read_csv('movies_df.csv', sep=';')
df_genres = pd.read_csv('movies_genres.csv', sep=';')

query = """SELECT DISTINCT
              T2.imdb_id, T2.poster_path, T2.genres_name
       FROM (SELECT 
                     T0.imdb_id,
                     T0.poster_path,
                     T1.genres_name,
                     row_number() over(partition by T0.imdb_id) AS RK
              FROM df_movies AS T0
              INNER JOIN df_genres AS T1
              ON T0.imdb_id = T1.imdb_id 
              ) AS T2
       WHERE RK = 1;"""

df = sqldf(query)

url = df['poster_path']
filename = df['imdb_id']
genre = df['genres_name']


def dowload_poster(url,filename,genre):
    ## Set up the image URL and filename
    image_url = "https://www.themoviedb.org/t/p/w600_and_h900_bestv2"+str(url)
    #filename = image_url.split("/")[-1]
    filename =  "posters" +'/'+ str(genre) +'/'+ str(filename)+".jpg"

    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream = True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        
        if not os.path.exists("posters" +'/'+ str(genre)):
            os.makedirs("posters" +'/'+ str(genre))

        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            
        print('Image sucessfully Downloaded: ',filename)
    else:
        print('Image Couldn\'t be retreived')

# loop to use the fuction in each image link
for url,filename,genre in zip(url,filename,genre):
    dowload_poster(url,filename, genre)




# Lembrar de tirar os IMDB_ID NaN
# Entender a melhor maneira de salvar os dados rotulados (filtrar por genero)
