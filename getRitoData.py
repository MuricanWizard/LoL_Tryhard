import requests

api_key = open('key.txt', 'r').read()

switch = 0

while(switch == 0):
    try:
        gameData = requests.get('https://127.0.0.1:2999/liveclientdata/playerlist', verify=False).json()
        switch = 1
    except:
        switch = 0

while(len(gameData) != 10):
    gameData = requests.get('https://127.0.0.1:2999/liveclientdata/playerlist', verify=False).json()

summoners = []
champs = []
for i in gameData:
    summoners.append(i['summonerName'])
    champs.append(i['championName'])

playerIDs = []
summonerLevels = []
for i in range(10):
    try:
        response = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+summoners[i]+"?api_key="+api_key)
        userID = response.json()["id"]
        puuid = response.json()["puuid"]
        summonerLevel = response.json()["summonerLevel"]
        playerIDs.append(userID)
        summonerLevels.append(summonerLevel)
    except:
        playerIDs.append("NA")
        summonerLevels.append("NA")

champSet = set(("Aurelion Sol", "Cho'Gath", "Dr. Mundo", "Jarvan IV", "Kai'Sa", "Kha'Zix", "Lee Sin", "Kog'Maw", "Miss Fortune", "Nunu & Willump", "Rek'Sai", "Tahm Kench", "Twisted Fate", "Vel'Koz", "Xin Zhao", 'LeBlanc', 'Wukong', 'Master Yi'))
champConvertDict = {
    "Aurelion Sol": "AurelionSol",
    "Cho'Gath": "Chogath",
    "Dr. Mundo": "DrMundo",
    "Jarvan IV": "JarvanIV",
    "Kai'Sa" : "Kaisa",
    "Kha'Zix" : "Khazix",
    "Lee Sin" : "LeeSin",
    "Kog'Maw" : "KogMaw",
    "Miss Fortune" : "MissFortune",
    "Nunu & Willump" : "Nunu",
    "Rek'Sai" : "RekSai",
    "Tahm Kench" : "TahmKench",
    "Twisted Fate" : "TwistedFate",
    "Vel'Koz" : "Velkoz",
    "Xin Zhao" : "XinZhao",
    "LeBlanc" : "Leblanc",
    "Wukong" : "MonkeyKing",
    "Master Yi" : "MasterYi"
}
def changeChamp(champName):
    if(champName in champSet):
        return(champConvertDict[champName])
    else:
        return(champName)
champions = requests.get("http://ddragon.leagueoflegends.com/cdn/10.22.1/data/en_US/champion.json")

champIDs = []
for i in champs:
    tempChamp = changeChamp(i)
    champIDs.append(champions.json()['data'][tempChamp]['key'])

champLevels = []
champPoints = []
for i in range(10):
    try:
        stats = requests.get('https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/'+str(playerIDs[i])+'/by-champion/'+str(champIDs[i])+'?api_key='+str(api_key)).json()
        champLevels.append(stats['championLevel'])
        champPoints.append(stats['championPoints'])
    except:
        champLevels.append('NA')
        champPoints.append('NA')

ranks = []
for i in playerIDs:
    try:
        rankStats = requests.get("https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/"+str(i)+"?api_key="+str(api_key))
        r = rankStats.json()[0]['rank']
        t = rankStats.json()[0]['tier']
        ret = str(t)+" "+str(r)
        ranks.append(ret)
    except:
        ranks.append("Unranked")

s = "<table id='summoners'><tr><th>Summoner Name</th><th>Team</th><th>Rank</th><th>Level</th><th>Champion</th><th>Champion Mastery Level</th><th>Champion Mastery Points</th></tr>"
for i in range(10):
    if(i < 5):
        s += "<tr id='ally'>"
    else:
        s += "<tr>"
    s += "<td>"+str(summoners[i])+"</td>"
    if(i < 5):
        s += "<td>"+str(1)+"</td>"
    else:
        s += "<td>"+str(2)+"</td>"
    s += "<td>"+str(ranks[i])+"</td>"
    s += "<td>"+str(summonerLevels[i])+"</td>"
    s += "<td>"+str(champs[i])+"</td>"
    s += "<td>"+str(champLevels[i])+"</td>" 
    s += "<td>"+str(champPoints[i])+"</td>"
    s += "</tr>"
s += "</table>"

print(s)
    