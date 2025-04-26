# z3_loader_local.py
import importlib.util
import os

# このローダーが存在するディレクトリ（＝core_1_mods）
BASE_DIR = os.path.dirname(__file__)

def load_z3_local_mods():
    mods_loaded = []
    for item in os.listdir(BASE_DIR):
        path = os.path.join(BASE_DIR, item)

        # 単体.pyファイル（z3系なら直接対応可能）
        if os.path.isfile(path) and item.endswith(".py") and item != os.path.basename(__file__):
            mod_name = item[:-3]
            spec = importlib.util.spec_from_file_location(mod_name, path)

        # フォルダ型Mod（__init__.pyを持っている）
        elif os.path.isdir(path) and os.path.exists(os.path.join(path, "__init__.py")):
            mod_name = item
            spec = importlib.util.spec_from_file_location(mod_name, os.path.join(path, "__init__.py"))

        else:
            continue  # スキップ

        try:
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            print(f"✅ [{mod_name}] 読み込み成功")
            mods_loaded.append(mod_name)
        except Exception as e:
            print(f"⚠️ [{mod_name}] 読み込み失敗: {e}")

    return mods_loaded

if __name__ == "__main__":
    load_z3_local_mods()
