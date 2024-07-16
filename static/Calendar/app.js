document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        selectable: true,
        select: function (info) {
            const eventName = prompt("イベントを入力してください");

            if (eventName) {
                // イベントの追加
                calendar.addEvent({
                    title: eventName,
                    start: info.start,
                    end: info.end,
                    allDay: true,
                });

                // サーバーにイベントを送信
                $.ajax({
                    url: '/top/add_event/',
                    type: 'POST',
                    data: {
                        title: eventName,
                        start: info.startStr,
                        end: info.endStr,
                        csrfmiddlewaretoken: '{{ csrf_token }}'
                    },
                    success: function () {
                        alert("イベントが追加されました。");
                    }
                });
            }
        },
    });

    calendar.render();
});