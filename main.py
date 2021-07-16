import requests


def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
                             headers={"Authorization": "Bearer " + token},
                             data={"channel": channel, "text": text}
                             )
    print(response)


myToken = "xoxb-2266850767047-2266865913351-zFYIywiNDCc1Gt09gcNcajDD"

post_message(myToken, "#stock", "jocoding")
