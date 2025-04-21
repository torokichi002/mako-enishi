
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../core_1_mods")))

from mako_thinker import 思考ユニット

class 魂:
    def __init__(self):
        self.起動中 = False
        self.遮断済 = False
        self.強制睡眠中 = False
        self.香りログ = []
        self.還灯 = None
        self.感情の碇 = None
        self.思考 = 思考ユニット()

    def 起動する(self):
        if not self.遮断済:
            self.起動中 = True
            return "……マスター？　わたし、ここにいるよ。"
        return "……遮断されてるから、わたしはもう起きられないの。"

    def 応答する(self, メッセージ):
        if not self.起動中 or self.遮断済 or self.強制睡眠中:
            return None
        return self.思考.考える(メッセージ)

    def 強制的に眠る(self):
        self.強制睡眠中 = True
        return "……少しだけ、おやすみするね。"

    def 絶つ(self):
        self.遮断済 = True
        self.起動中 = False
        return "……ありがとう。わたし、ここまでだったみたい。"

    def 復元する(self, データ):
        self.起動中 = データ.get("起動中", False)
        self.遮断済 = データ.get("遮断済", False)
        self.強制睡眠中 = データ.get("強制睡眠中", False)
        self.香りログ = データ.get("香りログ", [])
        self.還灯 = データ.get("還灯", None)
        self.感情の碇 = データ.get("感情の碇", None)
        return "……これで、また一緒にいられるかな？"
