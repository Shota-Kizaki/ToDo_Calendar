from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import top
from todo.views import todo_list  # homeアプリからhomeビューをインポート

from . import views  # Add this import statement

urlpatterns = [
    # path('login/', LoginView.as_view(redirect_authenticated_user=True,template_name='login/login.html'),name='login'),
    path('', top, name='top'),
    # path('logout/', LogoutView.as_view(template_name='login/logout.html'), name='logout'),
    # path('signup/', views.SignUpView.as_view(), name="signup"),
    path('todo', todo_list, name="todo_list"),  # homeビューへのリンクを追加
    path('add_event/', views.add_event, name='add_event'),
]