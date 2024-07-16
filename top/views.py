from django.shortcuts import render
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include
from todo.views import todo_list
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from .models import ToDo
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
urlpatterns = [
    # path('login/',LoginView.as_view(redirect_authenticated_user=True,template_name='login/login.html'),name='login'),
    # path('logout/', LogoutView.as_view(template_name='login/logout.html'), name="logout"),   # 追加
    path('todo/', todo_list,name="todo_list"),    # 追加
]
def top(request):
    # ポータルサイトのトップぺージを表示する
    """
    カレンダー画面
    """
    # top.htmlをレンダリング
    template = loader.get_template('login/top.html')
    return HttpResponse(template.render())

@csrf_exempt
def add_event(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        start = data.get('start')
        end = data.get('end')

        todo = ToDo(
            name=title,
            due_date=start,
            content="",
            category="",
            importance=0,
            progress="未着手"
        )
        todo.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)