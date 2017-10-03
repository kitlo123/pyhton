from flask import Flask, request
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "<p>Hello World!</p>"
   
@app.route('/callback', methods=['POST'])
def callback():
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    user = decoded['result'][0]['content']['from']
    text = decoded['result'][0]['content']['text']
    #print(json_line)
    print("使用者：",user)
    print("內容：",text)
    sendText(user,text)
    return 0

if __name__ == '__main__':
    app.run(debug=True)
