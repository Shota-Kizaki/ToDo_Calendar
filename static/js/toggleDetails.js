function completeEvent(eventId) {
    const situationElement = document.getElementById(`situation-${eventId}`);
    const situation = situationElement.textContent.trim();

    if (situation === '完了') {
        alert('このイベントはすでに完了しています。');
    } else {
        const confirmCompletion = confirm('このイベントを完了にしますか？');
        if (confirmCompletion) {
            // 完了処理をサーバーに送信
            window.location.href = `/todo_list_henshu/${eventId}/`;
        }
    }
}
