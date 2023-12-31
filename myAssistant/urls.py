"""
URL configuration for myAssistant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from blog.views import homepage, index_post, showpost, ads_view
from api.views import *
from blog.views import *

urlpatterns = [
    path('ads.txt', ads_view),
    path('admin/', admin.site.urls),
    path('', index_post),
    path('post/<str:slug>', showpost), # 定義視圖與參數名稱
    path('api/', test),
    path('api/doc/', apiTestView),
    path('sensor/save', sensor_data),
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import myAssistant.settings
if myAssistant.settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
