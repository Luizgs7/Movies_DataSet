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