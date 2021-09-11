#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 07 21:11:25 2021
@author: luizgsouza
"""

from os import sep
import requests
import pandas as pd
import numpy as np
from tmdb3 import set_key, set_cache

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

        ## Treating nested data
        # Genre by movieid
        try:
            genres = pd.json_normalize(
                    json_data,
                    sep = "_",
                    record_path=['genres'],
                    record_prefix='genres_',
                    meta=['imdb_id'],
                    #meta=['adult','backdrop_path','belongs_to_collection','budget','homepage','id','imdb_id','original_language','original_title','overview','popularity','poster_path','release_date','revenue','runtime','status','tagline','title','video','vote_average','vote_count'],
                    errors='ignore')
        except:
            print('genres doesnt exist')

        # production companies by movieid
        try:
            production_companies = pd.json_normalize(
                    json_data,
                    sep = "_",
                    record_path=['production_companies'],
                    record_prefix='pcompanies_',
                    meta=['imdb_id'],
                    #meta=['adult','backdrop_path','belongs_to_collection','budget','homepage','id','imdb_id','original_language','original_title','overview','popularity','poster_path','release_date','revenue','runtime','status','tagline','title','video','vote_average','vote_count'],
                    errors='ignore')
        except:
            print('production_companies doesnt exist')

        # production contries by movieid
        try:
            production_countries = pd.json_normalize(
                    json_data,
                    sep = "_",
                    record_path=['production_countries'],
                    record_prefix='pcountries_',
                    meta=['imdb_id'],
                    #meta=['adult','backdrop_path','belongs_to_collection','budget','homepage','id','imdb_id','original_language','original_title','overview','popularity','poster_path','release_date','revenue','runtime','status','tagline','title','video','vote_average','vote_count'],
                    errors='ignore')
        except:
            print('production_countries doesnt exist')

        # spoken languages by movieid
        try:
            spoken_languages = pd.json_normalize(
                    json_data,
                    sep = "_",
                    record_path=['spoken_languages'],
                    record_prefix='slanguages_',
                    meta=['imdb_id'],
                    #meta=['adult','backdrop_path','belongs_to_collection','budget','homepage','id','imdb_id','original_language','original_title','overview','popularity','poster_path','release_date','revenue','runtime','status','tagline','title','video','vote_average','vote_count'],
                    errors='ignore')
        except:
            print('spoken_languages doesnt exist')
        
        return df, genres, production_companies, production_countries, spoken_languages

# create dataframes
lst = []
lst_genres = []
lst_production_companies = []
lst_production_countries = []
lst_spoken_languages = []

for movieIndex in range(50000,50005):
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


# save data
dft.to_csv('movies_df.csv', index=False, sep=';')
genres.to_csv('movies_genres.csv', index=False, sep=';')
production_companies.to_csv('movies_production_companies.csv', index=False, sep=';')
production_countries.to_csv('movies_production_countries.csv', index=False, sep=';')
spoken_languages.to_csv('movies_spoken_languages.csv', index=False, sep=';')


