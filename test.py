import tmdb3 as t # uses https://github.com/wagnerrp/pytmdb3
from tmdb3 import set_key, set_cache, searchMovie, Movie
import pickle
import sys


import numpy as np
import pandas as pd
import requests
import json

t.set_key('e4242484419937005a3cab0a068c0ab0')
set_cache('null')

#b = t.searchMovie('A New Hope')
#print(b[0])
#print(b[1])
#print(b[2])


#p = Movie(11).poster
#print(p)


# List of channels we want to access
channels = [str(i).zfill(2) for i in range(500,505)]

channels_list = []
# For each channel, we access its information through its API
for channel in channels:
    JSONContent = requests.get("https://api.themoviedb.org/3/movie/" +channel+"?api_key=e4242484419937005a3cab0a068c0ab0").json()
    if 'error' not in JSONContent:
        print(JSONContent)
        channels_list.append([JSONContent['title'], JSONContent['vote_average'], JSONContent['backdrop_path']])

dataset = pd.DataFrame(channels_list)
dataset.columns = ['title', 'vote_average', 'backdrop_path']

#	https://www.themoviedb.org/t/p/w600_and_h900_bestv2/gQkzmZmZXIvvprfvvPE2EUlk121.jpg