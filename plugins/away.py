from cloudbot import hook

awaystatus = False

# TODO: Any user, checks and change state if user speaks

@hook.regex(r'(?i)(m|M)u5tank05(!| |\\.|\?)*')
def awayregex(nick, message):
    if awaystatus is False:
        return
    else:
        message("Sorry {}, but Mu5tank05 is currently away. Feel free to message him though".format(nick))


@hook.command()
def away(notice):
    global awaystatus
    if awaystatus is True:
        awaystatus = False
        notice("You are now here")
    elif awaystatus is False:
        awaystatus = True
        notice("You are now away")

