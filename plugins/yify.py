import requests

from cloudbot import hook
from cloudbot.util import web


@hook.command()
def yify(text):
    """(movie) - Returns YIFY info on movie """

    p = {'keywords': text, 'limit': '1'}
    r = requests.get('http://yts.re/api/list.json', params=p)
    j = r.json()

    if 'MovieList' in j:
        for movie in j['MovieList']:
            name = movie['MovieTitle']
            genre = movie['Genre']
            quality = movie['Quality']
            size = movie['Size']
            url = movie['MovieUrl']
            return "\x02{}\x02 Genre: {} - Quality: {} Size: {} - {}".format(name, genre, quality, size,
                                                                             web.try_shorten(url))
    else:
        return "Error: {}".format((j['error']))


