import urllib.request, json
from bs4 import BeautifulSoup

user_id = list()

def get_id():

    username = str(input('Enter username: '))

    data = urllib.request.urlopen(f'https://users.roblox.com/v1/users/search?keyword={username}&limit=10')
    data_load = json.loads(data.read().decode())

    for dic in data_load['data']:
        user_id.append(dic['id']) 

def get_info():

    data = urllib.request.urlopen(f'https://users.roblox.com/v1/users/{user_id[0]}')
    data_load = json.loads(data.read().decode())