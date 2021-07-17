import requests
from bs4 import BeautifulSoup as bs


url = 'https://finance.naver.com/sise/sise_rise.nhn'

res = requests.get(url)

soup = bs(res, 'html.parser')

print(soup)