from cloudbot import hook
import datetime

@hook.command(autohelp=False)
def death(message):
    """provides a motto for life"""
    td = datetime.datetime(2018, 5, 15) - datetime.datetime.now()
    message("There is {} day(s) until I finally fucking die".format(str(td.days)))
	
@hook.regex(r'.*(?i)(w|W)alter (how) (long) (till) (you) (die)(!| |\\.|\?)*')
def death_regex(message=None, nick=None):
    td = datetime.datetime(2018, 5, 15) - datetime.datetime.now()
    message("There is {} day(s) until I finally fucking die".format(str(td.days)))