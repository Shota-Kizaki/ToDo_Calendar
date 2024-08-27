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
from datetime import timedelta
from django.utils import timezone

# Create your views here.
urlpatterns = [
    path('', include('top.urls')),
    path('', include('todo.urls')),
]

def index(request):
    # 今日の日付を取得
    today = timezone.now().date()
    three_days_later = today + timedelta(days=3)

    # 今日から3日以内に締め切りがあるイベントをフィルタリング
    events = ToDo.objects.filter(end_date__gte=today, end_date__lte=three_days_later)

    return render(request, 'login/top.html', {'events': events})