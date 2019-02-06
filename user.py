import requests
from contextlib import closing
from bs4 import BeautifulSoup

# the order of the forum results - for now it doesn't really matter what order
DEF_ORDER = "asc"

base_url = 'https://archive.froast.io'

# gets the href for the archive with the id of the given username
def get_id_url(name):
    try:
        data = {
            'username': name,
            'order': DEF_ORDER
        }
        val = requests.get(base_url+'/api/search-user', params=data)
        return val.json()['redirect']
    except:
        print('Username not found or failed connection, whoops!')
        quit()

# user class capturing the logic for a the webpages of a profile
class User:

    def __init__(self, name):
        """
        typeof name is String

        """
        self.name = name

    # returns a list of all the forum posts that this user made
    def get_posts(self):
        id_url = get_id_url(self.name)
        curr_html = requests.get(base_url+id_url).text
        soup = BeautifulSoup(curr_html, 'html.parser')
        res = []

        while 1:
            for topic in soup.find_all("div", {"class": "Topic"}):
                href = topic.find("a").get('href').split('#')[0].split('/')[2]
                res.append(href)
                # print(href)
            last_pg_button = soup.find_all("div", {"class": "Forward-Full Link-Disabled Show"})
            if (len(last_pg_button) != 0):
                break
            next_href = soup.find_all("a", {"class": "Forward Link-Enabled"})[0].get('href')
            curr_html = requests.get(base_url+next_href).text
            soup = BeautifulSoup(curr_html, 'html.parser')


        return res

        
