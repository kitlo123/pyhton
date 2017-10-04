from flask import Flask, request, abort
from line import LineClient
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

def _getProfile(self):
        """Get profile information
        :returns: Profile object
                    - picturePath
                    - displayName
                    - phone (base64 encoded?)
                    - allowSearchByUserid
                    - pictureStatus
                    - userid
                    - mid # used for unique id for account
                    - phoneticName
                    - regionCode
                    - allowSearchByEmail
                    - email
                    - statusMessage
        """
        return self._client.getProfile()

 def _getContacts(self, ids):
        """Get contact information list from ids
        :returns: List of Contact list
                    - status
                    - capableVideoCall
                    - dispalyName
                    - settings
                    - pictureStatus
                    - capableVoiceCall
                    - capableBuddy
                    - mid
                    - displayNameOverridden
                    - relation
                    - thumbnailUrl
                    - createdTime
                    - facoriteTime
                    - capableMyhome
                    - attributes
                    - type
                    - phoneticName
                    - statusMessage
        """
        if type(ids) != list:
            msg = "argument should be list of contact ids"
            self.raise_error(msg)

        return self._client.getContacts(ids)
    
def weather():
    r = requests.get('http://www.hko.gov.hk/wxinfo/currwx/currentc.htm')
    print(r.text)
    x = r.text
    return x

def Test():
    y = 'hello world'
    return y

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("event.reply_token:", event.reply_token)
    print("event.message.text:", event.message.text)
    if event.message.text == "Test":
        content = Test()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return y

if event.message.text == "weather":
        content = weather()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return x

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
