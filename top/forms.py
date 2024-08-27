from django import forms
from .models import ToDo  # ToDoモデルをインポート

class EventForm(forms.ModelForm):
    start_date = forms.IntegerField(required=True)
    end_date = forms.IntegerField(required=True)
    event_name = forms.CharField(required=True, max_length=32)
    memo = forms.CharField(required=False, max_length=200)
    situation = forms.CharField(required=False, max_length=200)

    class Meta:
        model = ToDo  # ここでToDoモデルを指定
        fields = ['event_name', 'start_date', 'end_date', 'memo', 'situation']
