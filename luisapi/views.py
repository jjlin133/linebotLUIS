from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent
from module import func

################################################################
# 2021.0324_增加的內容 
#      ~~~ 來自 (GitHub Django 專案: firstproject\myapp\views.py)
from django.shortcuts import render
from datetime import datetime
from linebot.models import *
################################################################

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

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
