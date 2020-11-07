from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os

app = Flask(__name__)

#環境変数
ACCES_TOKEN = os.environ['cMd9wgdufzWuZdfJ6QYYi2flvfEH1NeNPJH2FgSnaMIRNc7i8o5OCysA6jt5zjZb2Ekfd7H6mJY / WusAbUdrqzy1 + UkkjIZOjq7wo9IQ + VocrrXoM']
SECRET = os.environ[]

line_bot_api = LineBotApi('')
