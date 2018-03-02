from cloudbot import hook
from cloudbot.util import http
# https://raw.githubusercontent.com/AwesomePowered/CloudBot/e01b2ab41985db8dbd6f6a1501ab9353f326188f/plugins/theyfightcrime.py
@hook.command("tfc")
def plot():
    bold = "\x02"
    try:
        soup = http.get_soup("http://www.theyfightcrime.org")
        plot = soup.find('table').find('p').text
        return bold + plot + bold
    except:
        return "Could not get plot."