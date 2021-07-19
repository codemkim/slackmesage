import requests
from bs4 import BeautifulSoup as bs
import time
from datetime import datetime


def set_message():
    # 시크릿 키 가져오기
    with open('.env') as f:
        read = f.readline()

    # 슬랙 api 토큰 주소
    myToken = read

    # 슬랙 채널명
    channel_name = '#stock'

    return myToken, channel_name

# 파이썬에서 슬랙으로 메시지 보내는 함수
def post_message(text):
    token, channel = set_message()
    response = requests.post("https://slack.com/api/chat.postMessage",
                             headers={"Authorization": "Bearer " + token},
                             data={"channel": channel, "text": text}
                             )
    print(response)


# 주소 받아오기
def get_soup(company_code):
    # 네이버 금융 url
    url = 'https://finance.naver.com/item/main.nhn?code='+company_code

    # requests를 통한 url 받아오기
    res = requests.get(url)

    # 파이썬에서 사용가능하도록 html로 변환
    soup = bs(res.content, 'html.parser')

    return soup

# 가격정보 받아오기
def get_price(company_code):
    soup = get_soup(company_code)

    today_s = soup.find('p', {'class':'no_today'})

    blind_s = today_s.find('span', {'class':'blind'})

    return blind_s.text.replace(',', '')


# 상승 / 하락 %
max_p = 0.001
min_p = 0.001

# 나의 평단
first_price = 79800

# 목표 가격
target_max_price = first_price + (first_price * max_p)
target_min_price = first_price - (first_price * min_p)


# 자동 알림 코드

while True:
    s_price = int(get_price('005930'))


    if s_price >= target_max_price:
        now = str(datetime.now())
        post_message(f'삼성전자 : {str(s_price)} / 시간 : {now[:-6]}')

        target_max_price = s_price + (first_price * max_p)

        target_min_price = s_price - (first_price * min_p)

        print(target_max_price, target_min_price)

    elif s_price <= target_min_price:
        now = str(datetime.now())
        post_message(f'삼성전자 : {str(s_price)} / 시간 : {now[:-6]}')

        target_max_price = s_price + (first_price * max_p)

        target_min_price = s_price - (first_price * min_p)

        print(target_max_price, target_min_price)

    time.sleep(20)


