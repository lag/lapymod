from requests import get
from json import loads
from .humanize import getHumanized
from uuid import UUID

class User:

    def getAllData(self):
        r = {}
        r['emotes'] = self.getEmotes()
        r['roles'] = self.getRoles()
        r['cosmetics'] = self.getCosmetics()
        r['stickers'] = self.getStickers()
        return r

    def getEmotes(self):
        if 'e' in self._data.keys():
            return getHumanized('emotes',self._data['e'])
        return []

    def getRoles(self):
        if 'g' in self._data.keys():
            roles = []
            for role in self._data['g']:
                roles.append(role['i'])
            return getHumanized('roles',roles)
        return []

    def getCosmetics(self):
        if 'c' in self._data.keys():
            cosmetics = []
            for cosmetic in self._data['c']:
                cosmetics.append(cosmetic['i'])
            return getHumanized('cosmetics',cosmetics)
        return []

    def getStickers(self):
        if 'st' in self._data.keys():
            if 'p' in self._data['st'].keys():
                stickers = self._data['st']['p']
                return getHumanized('stickers',stickers)
        return []

    def setUser(self,uuid):
        self._uuid = UUID(uuid)
        if uuid != None:
            return True
        else:
            raise AttributeError("User must be given a UUID.")

    def update(self):
        r = get("https://dl.labymod.net/userdata/{}.json".format(self._uuid))
        try:
            self._data = loads(r.content)
        except:
            raise Exception("User has not used Labymod.")
        return self._data

    def __init__(self,uuid=None):
        self.setUser(uuid)
        self.update()
