from django.db import models

class ToDo(models.Model):
    number = models.AutoField(primary_key=True)
    due_date = models.DateTimeField(verbose_name='期限日付')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新日')
    name = models.CharField(max_length=255, verbose_name='ToDo名')
    content = models.TextField(verbose_name='内容')
    category = models.CharField(max_length=100, verbose_name='カテゴリー')
    importance = models.IntegerField(verbose_name='重要度')
    progress = models.CharField(max_length=100, verbose_name='進行状況')

    def __str__(self):
        return self.name