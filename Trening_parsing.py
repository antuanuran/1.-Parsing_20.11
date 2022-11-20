import requests
url = 'https://netology.ru/blog/'
response = requests.get(url)

from pprint import pprint
from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, 'html.parser')
list = soup.find_all('div', class_='posts__item')


for res in list:
    title = res.find('a', class_='posts__link').text
    print(title)

# Второй комит




