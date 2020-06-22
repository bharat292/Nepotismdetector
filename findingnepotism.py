import requests
import bs4
name = input('enter the name of the actor/actress')
name.replace(' ','_')
res = requests.get(f'https://en.wikipedia.org/wiki/{name}')
#res.text
soup = bs4.BeautifulSoup(res.text, 'lxml')
for x in soup.find_all('p'):
    if 'was born on' in x.text:
        for y in ['director','producer','actor','actress','directors','producers','actresses',
                 'actors','singer','filmmaker']:
            if (' ' + y + ' ') in (' ' + x.text + ' '):
                print('Yes nepotism founded')
                break