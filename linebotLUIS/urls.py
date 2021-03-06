"""linebotLUIS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from luisapi import views

########################################################
### 2021.0320 add import from ref :
#https://docs.djangoproject.com/en/2.0/howto/static-files/
from django.conf import settings
from django.conf.urls.static import static
#from luisapi.views import sayhello,hello3,hello4,fv,fv2,index
########################################################

urlpatterns = [
#    url('callback', views.callback),
    url('callback',include('luisapi.urls'))
    path('admin/', admin.site.urls),
    url(r'^$', views.sayhello),
    url(r'^hello3/(\w+)/$', views.hello3),
    url(r'^hello4/(\w+)/$', views.hello4),
    url(r'^fv/$', views.fv),		
    url(r'^fv2/$', views.fv2),

]

# 2021.0320 合併2個API -- 
# (1)主軸 : Django GitHub 專案(linebotLUIS\luisapi 
#          LINE Bot 機器人匯率查詢專案 currency 
# (2)附加 : 計算本利和網頁(templates\fv\fv & templates\fv\fv2)
#           -- 來自 GitHub Django 專案(firstproject)

############new but not works #############################
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#urlpatterns += staticfiles_urlpatterns()
