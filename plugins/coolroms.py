from cloudbot import hook
from cloudbot.util import web

systems = [
    'atari2600',
    'atari5200',
    'atari7800',
    'atarijaguar',
    'atarilynx',
    'c64',
    'cps1',
    'cps2',
    'gba',
    'gbc',
    'mame',
    'namcosystem22',
    'neogeo',
    'neogeocd',
    'neogeopocket',
    'nes',
    'n64',
    'nds',
    'gcn',
    'segacd',
    'dc',
    'gamegear',
    'genesis',
    'mastersystem',
    'model2',
    'saturn',
    'psx',
    'ps2',
    'snes'
]


@hook.command('roms')
@hook.command('cr')
@hook.command()
def coolrom(text):
    """coolrom [system] [romname] returns a search result of coolrom.com.au"""
    query = text.split(' ', 1)
    if query[0] not in list(systems):
        return 'Please include a valid system'
    elif len(query) == 1:
        return "Please include a system and romname"
    else:
        system = query[0].lower()
        romname = query[1].strip()
        link = "http://coolrom.com.au/search?system={}&q={}".format(system, romname)
        return web.try_shorten(link)


@hook.command(autohelp=False)
def coolromsys(text):
    return "Systems Supported: " + ", ".join(map(str, systems))