from django.conf import settings

from linebot import LineBotApi
from linebot.models import TextSendMessage

import requests
import twder  #匯率套件

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

currencies = {'美金':'USD','美元':'USD','港幣':'HKD','英鎊':'GBP','澳幣':'AUD','加拿大幣':'CAD',\
              '加幣':'CAD','日圓':'JPY','日幣':'JPY','歐元':'EUR','韓元':'KRW',\
              '韓幣':'KRW','人民幣':'CNY' }  #幣別字典
keys = currencies.keys()

def sendUse(event):  #使用說明
    try:
        text1 ='''
查詢匯率：輸入外幣名稱「XXXX」，例如「美金」,「英鎊」,「港幣」,「澳幣」,「日圓」,「歐元」,「人民幣」
               '''
        message = TextSendMessage(
            text = text1
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

#函數 sendLUIS 是課本Ch09 範例 >>> 可以修正為自己的函數 sendTWder

def sendTWder(event, mtext):  
    try:
#        money = '美元'
        money = mtext
        if not money == '':  #匯率類幣別存在
            if money in keys:
                rate3 = float(twder.now(currencies[money])[3])  #由匯率套件取得匯率
                message = money + '_即期買入匯率 : ' + str(rate3)+ '_(台灣銀行端) '
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
            else:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='無此幣別匯率資料！'))
        else:  #其他未知輸入
            text = '無法了解你的意思，請重新輸入！'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text))
            
    except:
       line_bot_api.reply_message(event.reply_token, TextSendMessage(text='執行時產生錯誤！'))

def neuWeb(event):  #網頁連結
    try:
        text1 ='''
北歐福利網頁：https://kknews.cc/zh-tw/world/3q2r8ng.html

西歐 藍眼睛的邂逅 網頁：
http://172.104.79.148/mcu/?act=shopping&cmd=main&pg_id=2020093000011
               '''
        message = TextSendMessage(
            text = text1
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

		
def sendButton(event):  #按鈕樣版
    try:
        message = TemplateSendMessage(
            alt_text='@北歐貿易',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/4QfKuz1.png',  #顯示的圖片
                title='北歐貿易',  #主標題
                text='丹麥-瑞典-芬蘭-挪威',  #副標題
                actions=[
                    URITemplateAction(  #開啟網頁
                        label='貨幣轉換網頁',
                        uri='https://zt.coinmill.com/'
                    ),
                    URITemplateAction(  #開啟網頁
                        label='北歐福利網頁',
                        uri='https://kknews.cc/zh-tw/world/3q2r8ng.html'
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
		
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='sendButton 發生錯誤！'))
