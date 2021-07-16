import requests

# 파이썬에서 슬랙으로 메시지 보내는 함수
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
                             headers={"Authorization": "Bearer " + token},
                             data={"channel": channel, "text": text}
                             )
    print(response)

# 시크릿 키 가져오기
with open('.env') as f:
    read = f.readline()

# 슬랙 api 토큰 주소
myToken = read

# 슬랙 채널명
channel_name = '#stock'

# 보낼 메시지
text = 'muuuuuyaaaho'

# 메시지 전송 함수 호출
post_message(myToken, channel_name, text)

