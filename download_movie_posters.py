## Importing Necessary Modules
import requests # to get image from the web
import shutil # to save it locally
import pandas as pd # to import csv file

df = pd.read_csv('movies_df.csv', sep=';')
url = df['poster_path']
filename = df['imdb_id']

def dowload_poster(url,filename):
    ## Set up the image URL and filename
    image_url = "https://www.themoviedb.org/t/p/w600_and_h900_bestv2"+str(url)
    #filename = image_url.split("/")[-1]
    filename = str(filename)+".jpg"

    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream = True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        
        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            
        print('Image sucessfully Downloaded: ',filename)
    else:
        print('Image Couldn\'t be retreived')

# loop to use the fuction in each image link
for url,filename in zip(url,filename):
    dowload_poster(url,filename)




# Lembrar de tirar os IMDB_ID NaN
# Entender a melhor maneira de salvar os dados rotulados (filtrar por genero)
