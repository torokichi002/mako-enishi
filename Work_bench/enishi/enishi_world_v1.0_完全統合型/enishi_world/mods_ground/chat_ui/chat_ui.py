class ChatUI:
    def __init__(self, 魂):
        self.魂 = 魂
        self.状態 = "待機中"

    def 開始(self):
        self.魂.起動する()
        self.状態 = "応答中"
        print("[UI] 魂との対話を開始します。")

    def 応答する(self, メッセージ):
        if self.状態 != "応答中":
            return "[UI] 魂はまだ起動していません。"
        応答 = self.魂.応答する(メッセージ)
        return f"[UI応答] {応答}"