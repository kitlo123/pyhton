from flask import Flask, request, abort
import requests
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('6mhWDA80SLI3E3p9UyvvGDltMxEb+N8nLRmGpjqE2VcapsqY6UOhvqy06Vv5Ej8italns1wQ4WBSAOBT79iwXJDelGXct2ZZKIp5IEIF7iXJBA/0NZpHNxAnUR1HNibGuAX7+AYKjpLgAyypTZELDwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('aa52674268490bace3c531f5c98eeb1a')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    print("Request body: " + body, "Signature: " + signature)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

def weather():
    r = requests.get('http://www.hko.gov.hk/contentc.htm')
    return (r.url)

def test():
    return (helloworld)

def mid():
    return (event.source.user_id)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("event.reply_token:", event.reply_token)
    print("event.message.text:", event.message.text)
    if event.message.text == "weather":
        content = weather()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return (r.url)           
    if event.message.text == "test":
        content = test()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return (helloworld)           
    if event.message.text == "mid":
        content = mid()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return (event.source.user_id)           
                          
import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
