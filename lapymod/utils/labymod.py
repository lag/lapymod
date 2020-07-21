from requests import get
from json import loads
from .humanize import getHumanized

def getShopEmotes():
    r = get('https://dl.labymod.net/advertisement/entries.json')
    j = loads(r.content)
    if 'dailyEmotes' in j.keys():
        emotes = []
        for emote in j['dailyEmotes']:
            emotes.append(emote['id'])
        return getHumanized('emotes',emotes)
    return None

def getStatus():
    r = get('https://dl.labymod.net/')
    try:
        j = loads(r.content)
        if 'status' in j.keys():
            if j['status'] == 'OK':
                return True
    except:
        pass
    return False
