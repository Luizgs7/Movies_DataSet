#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 21:11:25 2020
@author: luizgabriel
"""

import requests
import pandas as pd
import numpy as np
from tmdb3 import set_key, set_cache, searchMovie

set_key('e4242484419937005a3cab0a068c0ab0')
set_cache('null')

class MovieInfo:
    def __init__(self, movies_number):
        self.id = movies_number
        self.api = requests.get("https://api.themoviedb.org/3/movie/" + str(movies_number) + "?api_key=e4242484419937005a3cab0a068c0ab0")
        
    def basic_info(self):
        try:
            api = self.api
        except:
            print('movie doesnt exist')

        json_data = api.json()

        # basic movie info
        df = pd.json_normalize(
                json_data,
                sep = "_",
                #record_path=['genres'],
                #record_prefix='genres_',
                #meta=['imdb_id'],
                #meta=['adult','backdrop_path','belongs_to_collection','budget','homepage','id','imdb_id','original_language','original_title','overview','popularity','poster_path','release_date','revenue','runtime','status','tagline','title','video','vote_average','vote_count'],
                errors='ignore')
        df = df.drop(columns=["genres", "production_companies", "production_countries","spoken_languages"])
        value = df.loc[0,'imdb_id']

        def normalize_nested(column,sep):
            try:
                unested = pd.json_normalize(
                        json_data,
                        sep = "_",
                        record_path=[column],
                        record_prefix=column+sep,
                        meta=['imdb_id'],
                        #meta=['adult','backdrop_path','belongs_to_collection','budget','homepage','id','imdb_id','original_language','original_title','overview','popularity','poster_path','release_date','revenue','runtime','status','tagline','title','video','vote_average','vote_count'],
                        errors='ignore')
                return unested
            except:
                print(f'{column} doesnt exist')

        genres= normalize_nested("genres", '_')
        production_companies= normalize_nested("production_companies", '_')
        production_countries= normalize_nested("production_countries", '_')
        spoken_languages = normalize_nested("spoken_languages", '_')
        
        # #pega o tipo dos pokemons
        # df_types = pd.json_normalize(api.json(), record_path = 'genres', sep = "_", max_level = 1)
    
        # #testa se o pokemon possui dois Tipos         
        # try:
        #     type2 = pd.DataFrame([genres.iloc[1]])["genres_name"]
        # except:
        #     type2 = np.nan

        # data = {'genre1':pd.DataFrame([genres.iloc[0]])["genres_name"],
        #         'genre2':type2}
    
        # df_types = pd.DataFrame(data=data)
        # df_types['id'] = value
    
        # #Joga tudo para a mesma base de cadastro:
        #     #Infos unicas + Tipos
        #df = pd.merge(df, genres, on = 'imdb_id', how = 'left')
        
        return df, genres, production_companies, production_countries, spoken_languages

#Cria DataFrame com todos os filmes
lst = []
lst_genres = []
lst_production_companies = []
lst_production_countries = []
lst_spoken_languages = []

for movieIndex in range(5005,10505,10):
    try:
    
        movie = MovieInfo(movieIndex)
        
        df, genres, production_companies, production_countries, spoken_languages = movie.basic_info()
        
        lst.append(df)
        lst_genres.append(genres)
        lst_production_companies.append(production_companies)
        lst_production_countries.append(production_countries)
        lst_spoken_languages.append(spoken_languages)        

        print(movieIndex, df['title'])
    except:
        print("Não encontrou:", movieIndex)

dft = pd.concat(lst)
genres = pd.concat(lst_genres)
production_companies = pd.concat(lst_production_companies)
production_countries = pd.concat(lst_production_countries)
spoken_languages = pd.concat(lst_spoken_languages)
#dft = dft[dft["success"] != False]
print(dft)

# save data
dft.to_csv('movies_df.csv', index=False)
genres.to_csv('movies_genres.csv', index=False)
production_companies.to_csv('movies_production_companies.csv', index=False)
production_countries.to_csv('movies_production_countries.csv', index=False)
spoken_languages.to_csv('movies_spoken_languages.csv', index=False)


# REF:
# https://towardsdatascience.com/all-pandas-json-normalize-you-should-know-for-flattening-json-13eae1dfb7dd


