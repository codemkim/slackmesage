import requests


def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
                             headers={"Authorization": "Bearer " + token},
                             data={"channel": channel, "text": text}
                             )
    print(response)


myToken = "xoxp-2266850767047-2305263783744-2294418003393-7fdef098d75a0bec073d5a907b6d0bd4"

text = '주환이 ㅎㅇ'

channel_name = '#stock'

post_message(myToken, channel_name, text)

