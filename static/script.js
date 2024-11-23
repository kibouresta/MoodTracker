document.getElementById('moodForm').addEventListener('submit', function(event) {
    event.preventDefault(); // フォーム送信を無効化

    const moodInput = document.getElementById('moodInput');
    const moodText = moodInput.value;

    fetch('/add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `moodInput=${encodeURIComponent(moodText)}`,
    })
    .then(response => response.json())
    .then(data => {
        const moodList = document.getElementById('moodList');
        const newMood = document.createElement('li');
        newMood.innerHTML = `${data.mood} - ${data.timestamp} 
            <button class="delete-btn" data-id="">削除</button>
            <button class="edit-btn" data-id="">編集</button>`;
        moodList.insertBefore(newMood, moodList.firstChild);
        moodInput.value = ''; // 入力フィールドをクリア
    })
    .catch(error => console.error('Error:', error));
});
