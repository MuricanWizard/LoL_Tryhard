import numpy as np
import pandas as pd
from keras import backend as K
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.models import model_from_json
import requests
from requests.auth import HTTPBasicAuth
from sys import argv
import warnings

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings("ignore")

champions = requests.get("http://ddragon.leagueoflegends.com/cdn/10.23.1/data/en_US/champion.json")
#Champion Dictionary
ChampionKeyTable = {}
for i in champions.json()['data']:
  champName = i
  champKey = champions.json()['data'][i]['key']
  ChampionKeyTable[int(champKey)] = champName


json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
'''
print("Loaded model from disk")
print("<br>")
'''

key = open('key.txt', 'r').read()
filePath = argv[1]
lockFile = ""

while(lockFile == ""):
    try:
        lockFile = open(filePath+'/lockFile', 'r').read()
    except:
        x = int(10)

lockFile = lockFile.split(":")

'''
print('Port: '+str(lockFile[2])+'<br> Password: '+str(lockFile[3])+'<br>')
'''
phase = "BAN_PICK"

while(str(phase) == str("BAN_PICK")):
    try:
        currentSess = requests.get('https://127.0.0.1:'+str(lockFile[2])+'/lol-champ-select/v1/session', verify=False, auth=HTTPBasicAuth('riot', str(lockFile[3])))
        phase = currentSess.json()['timer']['phase']
    except:
        x = int(20)

samiraStats = {
    'armor': 28,
    'armorperlevel': 3,
    'attackdamage': 59,
    'attackdamageperlevel': 2.3,
    'attackrange': 500,
    'attackspeed': 0.658,
    'attackspeedperlevel': 3.3,
    'mp': 348.88,
    'mpperlevel': 38,
    'hp': 530,
    'hpperlevel': 88,
    'hpregen': 3.25,
    'hpregenperlevel': 0.55,
    'movespeed': 335,
    'crit': 0,
    'critperlevel': 0,
    'mpregen': 8.176,
    'mpregenperlevel': 0.7,
    'spellblock': 30,
    'spellblockperlevel': 0.5
}
samiraInfo = {
    'attack': 8,
    'defense': 5,
    'difficulty': 6,
    'magic': 3
}

compStats = list()
if(1 == 1):
    currentSess = requests.get('https://127.0.0.1:'+str(lockFile[2])+'/lol-champ-select/v1/session', verify=False, auth=HTTPBasicAuth('riot', str(lockFile[3])))
    for i in currentSess.json()['myTeam']:
        champID = i['championId']
        if(champID == 360):
            champID = 999
            attack = samiraInfo['attack']
            defense = samiraInfo['defense']
            difficulty = samiraInfo['difficulty']
            magic = samiraInfo['magic']
            armor = samiraStats['armor']
            armorperlevel = samiraStats['armorperlevel']
            attackdamage = samiraStats['attackdamage']
            attackdamageperlevel = samiraStats['attackdamageperlevel']
            attackrange = samiraStats['attackrange']
            attackspeed = samiraStats['attackspeed']
            attackspeedperlevel = samiraStats['attackspeedperlevel']
            mp = samiraStats['mp']
            mpperlevel = samiraStats['mpperlevel']
            mpregenperlevel = samiraStats['mpregenperlevel']
            hp = samiraStats['hp']
            hpperlevel = samiraStats['hpperlevel']
            hpregen = samiraStats['hpregen']
            hpregenperlevel = samiraStats['hpregenperlevel']
            movespeed = samiraStats['movespeed']
            crit = samiraStats['crit']
            critperlevel = samiraStats['critperlevel']
            mpregen = samiraStats['mpregen']
            mpregenperlevel = samiraStats['mpregenperlevel']
            spellblock = samiraStats['spellblock']
            spellblockperlevel = samiraStats['spellblockperlevel']
        else:
            champName = ChampionKeyTable[int(champID)]
            attack = champions.json()['data'][champName]['info']['attack']
            defense = champions.json()['data'][champName]['info']['defense']
            difficulty = champions.json()['data'][champName]['info']['difficulty']
            magic = champions.json()['data'][champName]['info']['magic']
            armor = champions.json()['data'][champName]['stats']['armor']
            armorperlevel = champions.json()['data'][champName]['stats']['armorperlevel']
            attackdamage = champions.json()['data'][champName]['stats']['attackdamage']
            attackdamageperlevel = champions.json()['data'][champName]['stats']['attackdamageperlevel']
            attackrange = champions.json()['data'][champName]['stats']['attackrange']
            attackspeed = champions.json()['data'][champName]['stats']['attackspeed']
            attackspeedperlevel = champions.json()['data'][champName]['stats']['attackspeedperlevel']
            mp = champions.json()['data'][champName]['stats']['mp']
            mpperlevel = champions.json()['data'][champName]['stats']['mpperlevel']
            hp = champions.json()['data'][champName]['stats']['hp']
            hpperlevel = champions.json()['data'][champName]['stats']['hpperlevel']
            hpregen = champions.json()['data'][champName]['stats']['hpregen']
            hpregenperlevel = champions.json()['data'][champName]['stats']['hpregenperlevel']
            movespeed = champions.json()['data'][champName]['stats']['movespeed']
            crit = champions.json()['data'][champName]['stats']['crit']
            critperlevel = champions.json()['data'][champName]['stats']['critperlevel']
            mpregen = champions.json()['data'][champName]['stats']['mpregen']
            mpregenperlevel = champions.json()['data'][champName]['stats']['mpregenperlevel']
            spellblock = champions.json()['data'][champName]['stats']['spellblock']
            spellblockperlevel = champions.json()['data'][champName]['stats']['spellblockperlevel']
        compStats.append(champID)
        compStats.append(attack)
        compStats.append(defense)
        compStats.append(difficulty)
        compStats.append(magic)
        compStats.append(armor)
        compStats.append(armorperlevel)
        compStats.append(attackdamage)
        compStats.append(attackdamageperlevel)
        compStats.append(attackrange)
        compStats.append(attackspeed)
        compStats.append(attackspeedperlevel)
        compStats.append(mp)
        compStats.append(mpperlevel)
        compStats.append(hp)
        compStats.append(hpperlevel)
        compStats.append(hpregen)
        compStats.append(hpregenperlevel)
        compStats.append(movespeed)
        compStats.append(crit)
        compStats.append(critperlevel)
        compStats.append(mpregen)
        compStats.append(mpregenperlevel)
        compStats.append(spellblock)
        compStats.append(spellblockperlevel)
    for i in currentSess.json()['theirTeam']:
        champID = i['championId']
        if(champID == 360):
            champID = 999
            attack = samiraInfo['attack']
            defense = samiraInfo['defense']
            difficulty = samiraInfo['difficulty']
            magic = samiraInfo['magic']
            armor = samiraStats['armor']
            armorperlevel = samiraStats['armorperlevel']
            attackdamage = samiraStats['attackdamage']
            attackdamageperlevel = samiraStats['attackdamageperlevel']
            attackrange = samiraStats['attackrange']
            attackspeed = samiraStats['attackspeed']
            attackspeedperlevel = samiraStats['attackspeedperlevel']
            mp = samiraStats['mp']
            mpperlevel = samiraStats['mpperlevel']
            hp = samiraStats['hp']
            hpperlevel = samiraStats['hpperlevel']
            hpregen = samiraStats['hpregen']
            hpregenperlevel = samiraStats['hpregenperlevel']
            movespeed = samiraStats['movespeed']
            crit = samiraStats['crit']
            critperlevel = samiraStats['critperlevel']
            mpregen = samiraStats['mpregen']
            mpregenperlevel = samiraStats['mpregenperlevel']
            spellblock = samiraStats['spellblock']
            spellblockperlevel = samiraStats['spellblockperlevel']
        else:
            champName = ChampionKeyTable[int(champID)]
            attack = champions.json()['data'][champName]['info']['attack']
            defense = champions.json()['data'][champName]['info']['defense']
            difficulty = champions.json()['data'][champName]['info']['difficulty']
            magic = champions.json()['data'][champName]['info']['magic']
            armor = champions.json()['data'][champName]['stats']['armor']
            armorperlevel = champions.json()['data'][champName]['stats']['armorperlevel']
            attackdamage = champions.json()['data'][champName]['stats']['attackdamage']
            attackdamageperlevel = champions.json()['data'][champName]['stats']['attackdamageperlevel']
            attackrange = champions.json()['data'][champName]['stats']['attackrange']
            attackspeed = champions.json()['data'][champName]['stats']['attackspeed']
            attackspeedperlevel = champions.json()['data'][champName]['stats']['attackspeedperlevel']
            mp = champions.json()['data'][champName]['stats']['mp']
            mpperlevel = champions.json()['data'][champName]['stats']['mpperlevel']
            hp = champions.json()['data'][champName]['stats']['hp']
            hpperlevel = champions.json()['data'][champName]['stats']['hpperlevel']
            hpregen = champions.json()['data'][champName]['stats']['hpregen']
            hpregenperlevel = champions.json()['data'][champName]['stats']['hpregenperlevel']
            movespeed = champions.json()['data'][champName]['stats']['movespeed']
            crit = champions.json()['data'][champName]['stats']['crit']
            critperlevel = champions.json()['data'][champName]['stats']['critperlevel']
            mpregen = champions.json()['data'][champName]['stats']['mpregen']
            mpregenperlevel = champions.json()['data'][champName]['stats']['mpregenperlevel']
            spellblock = champions.json()['data'][champName]['stats']['spellblock']
            spellblockperlevel = champions.json()['data'][champName]['stats']['spellblockperlevel']
        compStats.append(champID)
        compStats.append(attack)
        compStats.append(defense)
        compStats.append(difficulty)
        compStats.append(magic)
        compStats.append(armor)
        compStats.append(armorperlevel)
        compStats.append(attackdamage)
        compStats.append(attackdamageperlevel)
        compStats.append(attackrange)
        compStats.append(attackspeed)
        compStats.append(attackspeedperlevel)
        compStats.append(mp)
        compStats.append(mpperlevel)
        compStats.append(hp)
        compStats.append(hpperlevel)
        compStats.append(hpregen)
        compStats.append(hpregenperlevel)
        compStats.append(movespeed)
        compStats.append(crit)
        compStats.append(critperlevel)
        compStats.append(mpregen)
        compStats.append(mpregenperlevel)
        compStats.append(spellblock)
        compStats.append(spellblockperlevel)
'''
for i in compStats:
    print(str(i))

print("<br>")
print("<br>")
print("<br>")
print("<br>")
'''
pred = loaded_model.predict_classes(np.array([compStats,]))[0]
if(pred == 1):
    print("Your team has a composition advantage. Your chances of winning are higher than the enemy's.<br>GO ALL OUT<br><br><a class='button' onClick = 'getPlayerStats();'>GET PLAYER STATS</a><br><a class='button' onClick = 'goHome();'>Go Home</a>")
elif(pred == 0):
    print("The enemy team has a composition advantage. Your chances of winning are lower than the enemy's.<br>PLAY SAFE<br><br><a class='button' onClick = 'getPlayerStats();'>GET PLAYER STATS</a><br><a class='button' onClick = 'goHome();'>Go Home</a>")
