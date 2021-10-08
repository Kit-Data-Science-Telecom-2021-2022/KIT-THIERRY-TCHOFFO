import requests
from bs4 import BeautifulSoup

def extract_beer_infos (url):
    infos = {
        'name': None,
        'note': None,
        'price': None,
        'volume': None,
    }
    
    #get page content 
    r = requests.get(url)

    # str en précisant un encodage
    content = r.content.decode('utf-8')
    soup = BeautifulSoup(content)

    #extraction des informations
    bear_infos =soup.find('div', attrs={'class': 'row detail-beer-variation'})
    
    infos['name']=bear_infos.find('h1').text
    infos['note']=int(bear_infos.find('div', attrs={'class':'stars'}).attrs['data-percent'])
    infos['note']=float(soup.find('span', attrs={'class':'price'}).text.split()[0].replace(',','.'))
    infos['volume']=int(bear_infos.find('span').text.split()[-2])

    return infos