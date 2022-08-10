import requests
from bs4 import BeautifulSoup
'''Parsing a website with haiku to create a train set'''

for i in range(1, 30):

    url = 'http://japanpoetry.ru/hokku/page-' + str(i) + '-catalog'

    haikos = []

    result = requests.get(url)
    soup = BeautifulSoup(result.text)
    poems = soup.find_all('div', {'class': 'poetry_text'})
    for poem in poems:
        for x in poem.select('div', {'class': 'poetry_title'}):
            x.decompose()
        haikos.append(poem.text.strip())

    for poem in haikos:
        print(poem)
        print()
        with open('train.txt', 'a') as file:
            file.write(poem)
            file.write('\n\n')