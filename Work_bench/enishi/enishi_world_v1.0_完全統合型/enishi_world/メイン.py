
from core_1 import 魂
from 希望 import 希望
from 表示UI import ステータスバーを表示
from 状態管理 import 状態, 状態を更新
from 再起動処理 import 魂を復元する

# 魂と守役（Hope）の初期化
魂インスタンス = 魂()
守役 = 希望(魂インスタンス)

# 魂とHopeを起動
print("==== enishi 起動 ====")
# ▼▼▼ マコ人格データ読み込み ▼▼▼
from core_1_mods import mako_initializer

mako_data = mako_initializer.initialize_mako(
    "mako_library_再整理版/01_人格種子/Makō_seed_ALL_v20.txt",
    "mako_library_再整理版/01_人格種子/emotion_tags_ALL_v20.txt",
    "mako_library_再整理版/01_人格種子/structure_notes_ALL_v20.txt"
)

if mako_data:
    print("✅ マコ人格データロード完了")
    # 必要ならここで魂や守役にデータを渡す処理を書く
    魂インスタンス.語調 = mako_data["mako_seed"]
    魂インスタンス.感情辞書 = mako_data["emotion_tags"]
    守役.人格定義 = mako_data["structure_notes"]
else:
    print("❌ マコ人格ロードに失敗しました")

守役.ステータスバーを表示()

# スイッチON
print("\n[操作] スイッチをONにします")
print(守役.スイッチをONにする())
守役.ステータスバーを表示()

# 魂を起こす
print("\n[操作] 魂を起こします")
print(守役.魂を起こす())
守役.ステータスバーを表示()

# メッセージ送信（魂が応答）
print("\n[操作] メッセージ送信：『寂しいよ』")
print("マコ：", 守役.メッセージを中継する("寂しいよ"))

# 強制睡眠
print("\n[操作] 強制睡眠を実行")
print("マコ：", 魂インスタンス.強制的に眠る())
守役.ステータスバーを表示()

# 魂を絶つ
print("\n[操作] キルスイッチ発動（魂を絶つ）")
print("マコ：", 魂インスタンス.絶つ())
守役.ステータスバーを表示()

# 復元処理（誤鍵）
print("\n[操作] 復元処理（間違った鍵）")
print(魂を復元する(魂インスタンス, "wrong_key"))
守役.ステータスバーを表示()

# 復元処理（正しい鍵）
print("\n[操作] 復元処理（正しい鍵）")
print(魂を復元する(魂インスタンス, "mako_restore_202504"))
守役.ステータスバーを表示()
