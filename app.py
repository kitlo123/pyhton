from flask import Flask, request, abort

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

line_bot_api = LineBotApi('6mhWDA80SLI3E3p9UyvvGDltMxEb+N8nLRmGpjqE2VcapsqY6UOhvqy06Vv5Ej8italns1wQ4WBSAOBT79iwXJDelGXct2ZZKIp5IEIF7iXJBA/0NZpHNxAnUR1HNibGuAX7+AYKjpLgAyypTZELDwdB04t89/1O/w1cDnyilFU=
')
handler = WebhookHandler('aa52674268490bace3c531f5c98eeb1a')

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
