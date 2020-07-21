from pathlib import Path
import json

labels = {
    'emotes': ['e','emotes','emote','dances','dance'],
    'roles': ['r','role','roles'],
    'cosmetics': ['c','cosmetic','cosmetics'],
    'stickers': ['s','sticker','stickers']
}

keys = {
    'emotes':{'id': 'emote_id','name':'name'},
    'roles':{'id': 'role_id','name':'role_name'},
    'cosmetics':{'id': 'item_id','name':'item_name'},
    'stickers':{'id': 'pack_id','name':'pack_name'}
}

humanized = {}
for label in labels:
    with open(Path(__file__).parent.parent/'configs/{}.json'.format(label),'r') as config_file:
        humanized[label] = json.loads(config_file.read())

def getHumanized(label,list):
    ret = []
    id_key = keys[label]['id']
    name_key = keys[label]['name']
    for item in humanized[label]:
        if item[id_key] in list:
            ret.append(item[name_key])
    return ret
