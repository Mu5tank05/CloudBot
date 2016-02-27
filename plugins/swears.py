import requests

from cloudbot import hook
from cloudbot.util import web


@hook.command()
def swear(text):
    """(word/phrase) - Returns if word/phrase is a considered offensive"""

    p = {'q': text}
    r = requests.get('http://www.wdyl.com/profanity', params=p)
    j = r.json()

    if j["response"] == "true":
        return "Unfortunately that word or phrase is considered offensive"
    else:
        return "Luckily for you that word or phrase is not considered offensive"


