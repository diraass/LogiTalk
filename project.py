import os
import subprocess
import time

html_content = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Чат Дмитра Духаньченка</title>
    <style>
        body { background-color: #1A1A1A; color: #FFFFFF; font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .chat-container { width: 100%; height: 100vh; background-color: #262626; display: flex; flex-direction: column; overflow: hidden; }
        .chat-messages { flex: 1; padding: 15px; overflow-y: auto; display: flex; flex-direction: column; gap: 10px; }
        .msg { max-width: 75%; padding: 8px 12px; border-radius: 8px; font-size: 14px; line-height: 1.4; }
        .msg.user { background-color: #007ACC; align-self: flex-end; }
        .msg.other { background-color: #333333; color: #FFFFFF; align-self: flex-start; }
        .input-area { display: flex; padding: 10px; background-color: #1F1F1F; gap: 10px; }
        input { flex: 1; background-color: #333333; border: none; border-radius: 6px; padding: 10px; color: white; font-size: 14px; outline: none; }
        button { background-color: #007ACC; color: white; border: none; border-radius: 6px; padding: 0 15px; font-weight: bold; cursor: pointer; }
        button:hover { background-color: #005999; }
    </style>
</head>
<body>
<div class="chat-container">
    <div class="chat-messages" id="chatBox"></div>
    <div class="input-area">
        <input type="text" id="userInput" placeholder="Напишіть повідомлення..." onkeydown="if(event.key==='Enter') sendMsg()">
        <button onclick="sendMsg()">==></button>
    </div>
</div>
<script>
const bc = new BroadcastChannel('dima_chat_channel');

bc.onmessage = function(event) {
    addMessage(event.data, 'other');
};

function sendMsg() {
    let input = document.getElementById('userInput');
    let text = input.value.trim();
    if(!text) return;

    input.value = '';

    if(text === '67') {
        text = 'СІКС СЕВЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕН';
    }

    addMessage(text, 'user');
    bc.postMessage(text);
}

function addMessage(text, side) {
    let chatBox = document.getElementById('chatBox');
    let msg = document.createElement('div');
    msg.className = 'msg ' + side;
    msg.innerText = text;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}
</script>
</body>
</html>
"""


def open_window():
    filename = "index_chat.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)

    file_path = os.path.abspath(filename)
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"

    if os.path.exists(chrome_path):
        subprocess.Popen([chrome_path, f"--app=file:///{file_path}", "--window-size=450,650"])
    elif os.path.exists(edge_path):
        subprocess.Popen([edge_path, f"--app=file:///{file_path}", "--window-size=450,650"])
    else:
        import webbrowser
        webbrowser.open(f"file:///{file_path}")


if __name__ == "__main__":
    open_window()
