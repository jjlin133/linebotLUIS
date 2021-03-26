from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from module import func

################################################################
# 2021.0324_增加的內容 
#      ~~~ 來自 (GitHub Django 專案: firstproject\myapp\views.py)
from django.shortcuts import render
from datetime import datetime
from linebot.models import *
################################################################

#~~~~~~~~~~2021. 修訂 加入 LINE Bot 專案(currency) 的資訊 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

from flask import Flask
from flask import request
from flask import abort

logger = logging.getLogger("django")

app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('17URPk56smrMsWCp7e912oZd81oLt9V54/XzaznpEi/zO5tPpacSIBG9LHVaczBdkg3yr082JtRH9P/jCVwQ1zjONXCtKBAXdZJPcwq7cstYc0fyACaO/0BI2qxkiaQi47L5anTlYck36ie8KK/kXAdB04t89/1O/w1cDnyilFU='
# 必須放上自己的Channel Secret
handler = WebhookHandler('7256e5990761221dad0a1047cb126934') #currency

line_bot_api.push_message('Uaa63a3f5feff2725536db7d81f09c929', TextSendMessage(text='已開啟Heroku連結'))
##########################~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##########

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                mtext = event.message.text
                if mtext=='@使用說明':  #顯示使用說明
                    func.sendUse(event)
                elif mtext=='@北歐貿易':  #顯示使用說明
                    func.neuWeb(event)

                else:  #一般性輸入
                    func.sendTWder(event, mtext)

        return HttpResponse()
    else:
        return HttpResponseBadRequest()
    
################################################################
# 2021.0324__增加函式定義
# Create your views here.
################################################################

# define sayhello
def sayhello(request):
   return HttpResponse("Hello Django!")

# define hello3
def hello3(request,username):
   now=datetime.now()
   return render(request,"hello3.html",locals())
   
# define hello4
def hello4(request,username):
   now=datetime.now()
   username="Jen-Jen Lin @2021.0320"
   return render(request,"hello4.html",locals()) 

# define fv
def fv(request):
   return render(request,"E_8_1_orig.html",locals()) 
   
# define fv2
def fv2(request):
   return render(request,"E_8_1.html",locals()) 
