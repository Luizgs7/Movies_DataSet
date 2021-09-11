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
        try:
            title = [JSONContent['title']
        except:
            title = ''
        title = movie.title
        # Error Handling for url-encoding non ascii titles!
        try:
            vote_average = [JSONContent['vote_average']
        except:
            continue
        channels_list.append([JSONContent['title'], JSONContent['vote_average'], JSONContent['backdrop_path']])

dataset = pd.DataFrame(channels_list)
dataset.columns = ['title', 'vote_average', 'backdrop_path']

#	https://www.themoviedb.org/t/p/w600_and_h900_bestv2/gQkzmZmZXIvvprfvvPE2EUlk121.jpg



from tmdb3 import set_key, set_cache, searchMovie
set_key('e4242484419937005a3cab0a068c0ab0')

set_cache('null')
#set_cache(filename='/full/path/to/cache') # the 'file' engine is assumed
#set_cache(filename='tmdb3.cache')         # relative paths are put in /tmp
#set_cache(engine='file', filename='~/.tmdb3cache')

#from tmdb3 import get_locale, set_locale
#get_locale()
#set_locale('br', 'br')

res = searchMovie('A New Hope')
print(res)


import tmdb3 as t # uses https://github.com/wagnerrp/pytmdb3
import pickle
import sys

t.set_key('YOUR API KEY')
b = t.searchMovie('a')
movies = []
for y in range(len(b)):
    try:
        sys.stdout.write(str(y)+',')
        x = b[y]
        # we want recent movies
        if x.releasedate.year < 1970:
            continue
        # and movies in English
        if 'English' not in [y.name for y in x.languages]:
            continue
        # and decent movies
        if x.releases['US'].certification not in [u'G',u'PG',u'PG-13']:
            continue
        movie = dict()
        movie['title'] = x.title
        movie['year'] = x.releasedate.year
        movie['date'] = x.releasedate
        movie['director'] = [y.name for y in x.crew if y.job == 'Director'][0] or 'Director Unknown'
        movie['poster'] = x.poster.geturl('w185')
        movie['rating'] = x.userrating
        movie['overview'] = x.overview
        movies.append(movie)
        print(len(movies))
    except KeyboardInterrupt:





[
    {
        "studentId": 1,
        "studentName": "James",
        "schools": [
            {
                "schoolId": 1,
                "classRooms": [
                    {
                        "classRoomId": {
                            "id": 1,
                            "floor": 2
                        }
                    },
                    {
                        "classRoomId": {
                            "id": 3
                        }
                    },
                ],
                "teachers": [
                    {
                        "teacherId": 1,
                        "teacherName": "Tom"
                    },
                    {
                        "teacherId": 2,
                        "teacherName": "Sarah"
                    }
                ]
            },
            {
                "schoolId": 2,
                "classRooms": [
                    {
                        "classRoomId": {
                            "id": 4
                        }
                    }
                ],
                "teachers": [
                    {
                        "teacherId": 1,
                        "teacherName": "Tom"
                    },
                    {
                        "teacherId": 2,
                        "teacherName": "Sarah"
                    },
                    {
                        "teacherId": 3,
                        "teacherName": "Tara"
                    }
                ]
            }
        ]
    }
]


classrooms = pd.io.json.json_normalize(json_data, ['schools', 'classRooms'], meta=[
    'studentId',
    'studentName',
    ['schools', 'schoolId']
])

teachers = pd.io.json.json_normalize(json_data, ['schools', 'teachers'], meta=[
    'studentId',
    ['schools', 'schoolId']
])

# Merge and rearrange the columns in the order of your sample output
classrooms.merge(teachers, on=['schools.schoolId', 'studentId']) \
    [['studentId', 'studentName', 'schools.schoolId', 'classRoomId.id', 'classRoomId.floor', 'teacherId', 'teacherName']]