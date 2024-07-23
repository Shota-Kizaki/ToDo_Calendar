from django.shortcuts import render
from top.models import ToDo
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from top.forms import EventForm
from datetime import datetime
import logging

# ロガーの設定
logger = logging.getLogger(__name__)

def todo_list(request):
    if request.method == "POST":
        event_name = request.POST.get('event_name')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        memo = request.POST.get('memo')
        situation = request.POST.get('situation')

        # ログにPOSTデータを出力
        logger.debug(f"Received POST data: {request.POST}")

        # 日付を変換
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

            # 開始日が終了日より後の場合、エラーメッセージを表示
            if start_date > end_date:
                raise ValueError("終了日は開始日より後でなければなりません。")

        except ValueError as e:
            # 日付の形式が無効または日付の順序が無効な場合、エラーメッセージを表示
            logger.error(f"Date validation error: {e}")
            return render(request, 'todo/todo_list.html', {
                'error_message': f'エラー: {str(e)}',
                'events': ToDo.objects.all().order_by('start_date'),
            })

        # 新しいイベントを作成して保存
        try:
            ToDo.objects.create(
                event_name=event_name,
                start_date=start_date,
                end_date=end_date,
                memo=memo,
                situation=situation
            )
            logger.debug("Event saved successfully")
        except Exception as e:
            logger.error(f"Error saving event: {e}")

        return redirect('todo_list')

    events = ToDo.objects.all().order_by('start_date')
    return render(request, 'todo/todo_list.html', {'events': events})
