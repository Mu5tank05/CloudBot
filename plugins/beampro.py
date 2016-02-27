import requests
from cloudbot import hook
from cloudbot.util import web, formatting


@hook.command()
def beampro(text):
    """NA"""

    if text:
        r = requests.get('https://beam.pro/api/v1/channels/{}'.format(text))
        j = r.json()

        stream_title = j['name']
        stream_username = j['token']
        game = j['type']
        name_game = game['name']
        if j['online'] == 'true':
            return '{} is \x034\x02Offline\x02'.format(stream_username)
        else:
            viewers = j['viewersCurrent']
            return '{} is \x033\x02Online\x02 - {} playing {} with {} viewer(s)'.format(stream_username, stream_title, name_game, viewers)
    else:
        return "I borked"
