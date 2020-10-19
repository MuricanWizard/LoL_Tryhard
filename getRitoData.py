import requests

key = open('key.txt', 'r').read()
data = requests.get('https://na1.api.riotgames.com/tft/summoner/v1/summoners/by-name/MuricanWizardv2?api_key='+str(key))
print(data.json()['id'])
