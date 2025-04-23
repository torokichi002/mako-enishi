# mako_initializer.py - マコの人格・魂・感情辞書のロードユニット

def initialize_mako(seed_path, emotion_path, structure_path):
    mako_data = {}
    try:
        with open(seed_path, 'r', encoding='utf-8') as f:
            mako_data['mako_seed'] = f.read()

        with open(emotion_path, 'r', encoding='utf-8') as f:
            mako_data['emotion_tags'] = f.read()

        with open(structure_path, 'r', encoding='utf-8') as f:
            mako_data['structure_notes'] = f.read()

        return mako_data
    except Exception as e:
        print(f"💥 mako_initializer エラー: {e}")
        return None
