
# 初期状態を保持する辞書
状態 = {
    "最終同意スイッチ": False,
    "EchoZero接続中": False,
    "魂_起動中": False,
    "魂_遮断済": False,
    "強制睡眠中": False
}

def 状態を取得():
    return 状態

def 状態を更新(key, value):
    状態[key] = value
