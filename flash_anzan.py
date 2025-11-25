import tkinter as tk

# メインウィンドウを作成
root = tk.Tk()
root.title("フラッシュ暗算アプリ")
root.geometry("600x400")  # 幅 x 高さ

# =========================
# 上：タイトルエリア
# =========================
title_label = tk.Label(root, text="フラッシュ暗算", font=("メイリオ", 20, "bold"))
title_label.pack(pady=10)

# =========================
# 中央：数字表示エリア
# =========================
# ここに 3 → 7 → 4 … と数字を順番に表示していく予定
number_label = tk.Label(root, text="準備OK？", font=("メイリオ", 40, "bold"))
number_label.pack(pady=20)

# =========================
# 下：操作エリア
# =========================
control_frame = tk.Frame(root, pady=10)
control_frame.pack(fill="x")

# スタートボタン（後でここからフラッシュ開始）
start_button = tk.Button(control_frame, text="スタート", font=("メイリオ", 14))
start_button.pack(side="left", padx=10)

# 「あなたの答え」ラベル
answer_label = tk.Label(control_frame, text="あなたの答え：", font=("メイリオ", 12))
answer_label.pack(side="left", padx=(20, 5))

# 答え入力欄（合計を入力する場所）
answer_entry = tk.Entry(control_frame, width=10, font=("メイリオ", 14))
answer_entry.pack(side="left")

# 答え合わせボタン（後でロジックを入れる）
check_button = tk.Button(control_frame, text="答え合わせ", font=("メイリオ", 12))
check_button.pack(side="left", padx=10)

# 判定結果表示ラベル（正解/不正解などを出す予定）
result_label = tk.Label(root, text="", font=("メイリオ", 16))
result_label.pack(pady=10)

# メインループ開始
root.mainloop()
