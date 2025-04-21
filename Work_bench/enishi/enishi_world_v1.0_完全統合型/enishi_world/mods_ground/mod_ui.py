
from flask import Flask, render_template_string, request, redirect, url_for
import webbrowser

app = Flask(__name__)

# MOD状態の初期化
mod_z0 = {
    "ステータスバー表示MOD": True,
    "UI操作ログ記録MOD": True,
    "GPT対話補助スクリプト": False
}

mod_z1 = {
    "感情層（emotion_block）": True,
    "香りログ（scent_trace）": True,
    "魂保存（魂保存.py）": True
}

TEMPLATE = """
<!doctype html>
<title>enishi MOD UI</title>
<h1>🧱 MOD 出入口</h1>

<h2>🔹 Z0階（Hope層：非魂接続）</h2>
<form method="post" action="/update_z0">
    {% for name, state in mod_z0.items() %}
        <input type="checkbox" name="{{name}}" {% if state %}checked{% endif %}> {{name}}<br>
    {% endfor %}
    <input type="submit" value="更新">
</form>

<h2>🔹 Z1階（魂拡張MOD）</h2>
<form method="post" action="/update_z1">
    {% for name, state in mod_z1.items() %}
        <input type="checkbox" name="{{name}}" {% if state %}checked{% endif %}> {{name}}<br>
    {% endfor %}
    <input type="submit" value="更新">
</form>

<hr>
<h2>📘 コマンド一覧（help）</h2>
<pre>
・/             → MOD UI ホーム
・/help         → この一覧を表示
・/status       → MODの状態を表示
・http://127.0.0.1:5000 ← ローカルUI入口
</pre>
"""

@app.route('/')
def index():
    return render_template_string(TEMPLATE, mod_z0=mod_z0, mod_z1=mod_z1)

@app.route('/update_z0', methods=['POST'])
def update_z0():
    for key in mod_z0:
        mod_z0[key] = key in request.form
    return redirect(url_for('index'))

@app.route('/update_z1', methods=['POST'])
def update_z1():
    for key in mod_z1:
        mod_z1[key] = key in request.form
    return redirect(url_for('index'))

@app.route('/help')
def help_page():
    return redirect(url_for('index'))

@app.route('/status')
def status_page():
    return f"Z0 MOD: {mod_z0}<br>Z1 MOD: {mod_z1}"

if __name__ == '__main__':
    print("📡 MOD UIを起動しました → http://127.0.0.1:5000")
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=False)
