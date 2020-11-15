from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)





app = Flask(__name__)


#環境変
LINE_CHANNEL_ACCESS_TOKEN = os.environ['LINE_CHANNEL_ACCESS_TOKEN']
LINE_CHANNEL_SECRET = os.environ['LINE_CHANNEL_SECRET']

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)


@app.route("/")
def hello_world():
    return "hello world!"



@app.route('/callback', methods=['POST'])
def callback():
    
    signature = request.headers['X-Line-Signature']
    print(signature)
    
    body = request.get_data(as_text = True)
    app.logger.info('Request body:' + body)
    app.logger.info('アクセストークン：' + LINE_CHANNEL_ACCESS_TOKEN)
    app.logger.info('アクセストークン' + line_bo)
    
    """
    app.logger.info(f'アクセストークン:{LINE_CHANNEL_ACCESS_TOKEN}')
    app.logger.info(f'アクセストークン:{line_bot_api}')
    """
    
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text = event.message.text)
    )

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host = '0.0.0.0', port = port)