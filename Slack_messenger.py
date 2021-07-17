import requests
from bs4 import BeautifulSoup as bs
import time

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





while True:
    s_price = int(get_price('005930'))

    if s_price > 80000:
        # 메시지 전송 함수 호출
        post_message(s_price)

    elif s_price <= 79000:
        # 메시지 전송 함수 호출
        post_message(s_price)

    elif s_price == 79800:
        post_message(s_price)

    time.sleep(5)
