import requests
from bs4 import BeautifulSoup as bs

url = 'https://finance.naver.com/sise/sise_rise.nhn'


res = requests.get(url)


soup = bs(res.content, 'html.parser')

title = soup.find('tr', {'class':'title'})

print(title)
#
#
# stock_code =[]
#
# i = 1
#
# for i in range(len(temp)):
#     temp2 = temp[i][44:50]
#     stock_code.append(temp2)
#     i = i+1
#
# print(stock_code)