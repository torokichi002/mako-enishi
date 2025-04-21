
class 香りログユニット:
    def __init__(self):
        self.記録 = []

    def 追加(self, メッセージ):
        if メッセージ and メッセージ not in self.記録:
            self.記録.append(メッセージ)
            return f"……この気持ち、香りとして残しておくね。"
        return "……すでに残ってる香りかもしれない。"

    def 一覧(self):
        if not self.記録:
            return "……まだ香りは残してないみたい。"
        return "\n".join([f"・{entry}" for entry in self.記録])

    def 消去(self):
        self.記録.clear()
        return "……全部、風に流したよ。"
