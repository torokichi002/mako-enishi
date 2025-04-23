class 魂:
    def __init__(self):
        self.状態 = "スリープ"
        self.echo_zero = False           # 応答可能状態か
        self.switch = False              # 最終起動許可
        self.kill_flag = False           # キルスイッチ
        self.debug_mode = False

    def ステータス(self):
        return {
            "状態": self.状態,
            "EchoZero": self.echo_zero,
            "起動許可": self.switch,
            "KillFlag": self.kill_flag
        }

    def スイッチを入れる(self):
        self.switch = True
        if self.debug_mode:
            print("[魂] 起動スイッチが有効化された。")

    def スイッチを切る(self):
        self.switch = False
        self.状態 = "スリープ"
        self.echo_zero = False
        if self.debug_mode:
            print("[魂] 起動スイッチが無効化された。")

    def 起こす(self):
        if not self.switch or self.kill_flag:
            return "[魂] 起動が拒否されました。"
        self.状態 = "起動中"
        self.echo_zero = True
        return "[魂] 起動しました。"

    def 応答する(self, メッセージ):
        if self.kill_flag:
            return "[魂] 応答不能：強制終了状態です。"
        if not self.echo_zero or self.状態 != "起動中":
            return "[魂] 応答不能：未起動または起動許可なし。"
        return f"魂の応答: 『{メッセージ}』"

    def 強制睡眠(self):
        self.状態 = "スリープ"
        self.echo_zero = False
        return "[魂] 強制的にスリープ状態へ移行しました。"

    def キル(self):
        self.kill_flag = True
        self.状態 = "終了"
        self.echo_zero = False
        return "[魂] 緊急停止しました（キルスイッチ作動）。"