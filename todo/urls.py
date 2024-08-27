from django.urls import path
from . import views
urlpatterns = [
    path('todo_list/', views.todo_list, name='todo_list'),
    path('todo_list_henshu/<int:event_id>/', views.todo_list_henshu, name='todo_list_henshu'),
    path('todo_narabikae', views.todo_narabikae, name='todo_narabikae'),
]