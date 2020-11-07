from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os

app = Flask(__name__)

#環境変数
ACCESS_TOKEN = os.environ['cMd9wgdufzWuZdfJ6QYYi2flvfEH1NeNPJH2FgSnaMIRNc7i8o5OCysA6jt5zjZb2Ekfd7H6mJY / WusAbUdrqzy1 + UkkjIZOjq7wo9IQ + VocrrXoM']
SECRET = os.environ['e262d76e7f872d0f53864429f5ae3100']

line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(SECRET)

@app.route('/callback', method=['POST'])
def callback():
    sig
