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

# 가격정보 받아오기(네이버)
def get_price(company_code):
    soup = get_soup(company_code)

    today_s = soup.find('p', {'class':'no_today'})

    blind_s = today_s.find('span', {'class':'blind'})

    return blind_s.text.replace(',', '')


# 상승 / 하락 확인 %
max_p = 0.001
min_p = 0.001

# 나의 평균 단가 및 투자 금액
first_price = 79800
my_money = 6623400

# 실시간 가격 확인
target_max_price = first_price + (first_price * max_p)
target_min_price = first_price - (first_price * min_p)


# 자동 알림 코드
while True:

    # 현재가격
    s_price = int(get_price('005930'))

    # 손익/손실
    persent = ( abs(first_price - s_price) / first_price )
    temp = str(my_money * persent)
    persent = str(persent * 100)

    # 현재시간
    now = str(datetime.now())

    # + / - 기호 설정
    if s_price >= first_price:
        sign = '+'
    else:
        sign = '-'

    # 실시간 가격 변동 알림
    if s_price >= target_max_price:

        # 메시지 전송
        post_message(f'손익(삼성) : {sign} {temp[:-2]}({sign}{persent[:4]}%) / 시간 : {now[10:-6]}')

        # 타겟 max/ min 값 지속 변경을 통한 실시간 알림
        target_max_price = s_price + (first_price * max_p)
        target_min_price = s_price - (first_price * min_p)

    elif s_price <= target_min_price:

        post_message(f'손익(삼성) : {sign} {temp[:-2]}({sign}{persent[:4]}%) / 시간 : {now[10:-6]}')

        target_max_price = s_price + (first_price * max_p)

        target_min_price = s_price - (first_price * min_p)

    time.sleep(60)


