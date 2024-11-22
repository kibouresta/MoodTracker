$(document).ready(function() {
    $('#moodForm').submit(function(event) {
        event.preventDefault();  // フォームのデフォルトの送信を防ぐ

        var moodInput = $('#moodInput').val();  // 入力値を取得

        $.ajax({
            url: '/add',  // サーバーのエンドポイント
            type: 'POST',  // POSTリクエストを送信
            data: { moodInput: moodInput },  // データをサーバーに送信
            success: function(response) {
                // サーバーからのレスポンスを利用して過去の記録に追加
                var moodText = response.mood;
                var moodEntry = $('<div>').text(moodText);
                $('#moodHistory').append(moodEntry);  // 新しい気分を履歴に追加
                $('#moodInput').val('');  // 入力フィールドをクリア
            },
            error: function() {
                alert('エラーが発生しました。もう一度試してください。');
            }
        });
    });
});
