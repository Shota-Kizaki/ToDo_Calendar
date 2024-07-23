from django.shortcuts import render
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse, JsonResponse, Http404
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import json
import time

from .models import ToDo
from .forms import EventForm
from todo.views import todo_list
from django.middleware.csrf import get_token

# Create your views here.
urlpatterns = [
    path('', include('top.urls')),
    path('', include('todo.urls')),
]

def index(request):
    # ポータルサイトのトップぺージを表示する
    """
    カレンダー画面
    """
    # CSRFのトークンを発行する
    get_token(request)
    # top.htmlをレンダリング
    template = loader.get_template('login/top.html')
    return HttpResponse(template.render())