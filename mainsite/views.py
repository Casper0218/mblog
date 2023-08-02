from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    post_lists = list()
    #把查詢資料從頭到尾看一次，並儲存成List結構
    #枚舉 #遍歷

    #數據處理 -->
    for count, post in enumerate(posts):
        post_lists.append("No.{}:".format(str(count+1)) + str(post)+"<br>") 
        post_lists.append("<small>"+str(post.body)+"</small><br><br>")
        post_lists.append("<small>"+str(post.slug)+"</small><br><br>")
    #資料表述方式
        #轉換成html代碼
    return HttpResponse(post_lists)

from datetime import datetime
def index(request):
    posts = Post.objects.all()
    now = datetime.now()
    number = 1 
    return render(request,'index.html',locals())
