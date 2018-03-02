import os
import asyncio
import codecs
import random

from cloudbot import hook
from cloudbot.util import colors


@hook.on_start()
def load_responses(bot):
    path = os.path.join(bot.data_dir, "ytb.txt")
    global responses
    with codecs.open(path, encoding="utf-8") as f:
        responses = [line.strip() for line in
                     f.readlines() if not line.startswith("//")]


@asyncio.coroutine
@hook.command("ytb","boys")
@hook.command(autohelp=False)
def yeahtheboys(message):
    """provides a motto for life"""
    response = random.choice(responses)
    message("{}".format(response))
	
@hook.regex(r'.*(?i)ytb.*|.*(?i)yeah the boys.*')
def ytb_regex(message=None, nick=None):
    message("YTB")
