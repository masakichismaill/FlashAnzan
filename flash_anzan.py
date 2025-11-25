import tkinter as tk
import random

root = tk.Tk()
root.title("フラッシュ暗算アプリ")
root.geometry("600x400")

# =========================
# フラッシュ用の内部データ
# =========================
NUM_COUNT = 5  # 何個の数字を見せるか（慣れたら増やしてOK）
INTERVAL_MS = 1000  # 何ミリ秒ごとに表示を切り替えるか（1000ms = 1秒）

numbers = []  # 例: [3, 7, 4, 9, 2]
total_sum = 0  # 上の合計
current_index = 0  # 今何番目を表示しているか（0,1,2,...）


def start_flash():
    """スタートボタンが押されたときに呼ばれる。
    問題を作って、数字のフラッシュ表示を開始する。
    """
    global numbers, total_sum, current_index

    # ランダムな1桁の数字を NUM_COUNT 個作る
    # 例: [3, 7, 4, 9, 2]
    numbers = [random.randint(1, 9) for _ in range(NUM_COUNT)]
    total_sum = sum(numbers)
    current_index = 0

    # 前回の答えや結果をクリア
    answer_entry.delete(0, tk.END)
    result_label.config(text="")

    # ボタン状態の整理
    start_button.config(state="disabled")  # フラッシュ中はスタートを押せないように
    check_button.config(state="disabled")  # まだ答え合わせはできない

    # まず1つ目を表示スタート
    show_next_number()


def show_next_number():
    """numbers[current_index] を表示し、
    まだ残りがあれば 1 秒後にもう一度この関数を呼ぶ。
    """
    global current_index

    if current_index < len(numbers):
        # 今の数字を表示
        number_label.config(text=str(numbers[current_index]))
        current_index += 1

        # 1秒後にもう一度この関数を呼ぶ
        root.after(INTERVAL_MS, show_next_number)
    else:
        # すべて表示し終わったらメッセージ変更
        number_label.config(text="合計を入力してね")
        # 答え合わせボタンを有効化
        check_button.config(state="normal")
        # スタートボタンも押せるように（連続で練習したい場合用）
        start_button.config(state="normal")


def check_answer():
    """答え合わせボタンが押されたときに呼ばれる。
    入力された値と total_sum を比較して判定する。
    """
    user_text = answer_entry.get().strip()
    if not user_text:
        result_label.config(text="答えを入力してね")
        return

    try:
        user_answer = int(user_text)
    except ValueError:
        result_label.config(text="数字で入力してね")
        return

    if user_answer == total_sum:
        result_label.config(text=f"正解！ 合計は {total_sum} です 🎉")
    else:
        result_label.config(text=f"残念… 正解は {total_sum} です")


# =========================
# 上：タイトルエリア
# =========================
title_label = tk.Label(root, text="フラッシュ暗算", font=("メイリオ", 20, "bold"))
title_label.pack(pady=10)

# =========================
# 中央：数字表示エリア
# =========================
number_label = tk.Label(root, text="準備OK？", font=("メイリオ", 40, "bold"))
number_label.pack(pady=20)

# =========================
# 下：操作エリア
# =========================
control_frame = tk.Frame(root, pady=10)
control_frame.pack(fill="x")

# スタートボタン
start_button = tk.Button(
    control_frame, text="スタート", font=("メイリオ", 14), command=start_flash
)
start_button.pack(side="left", padx=10)

# 「あなたの答え」ラベル
answer_label = tk.Label(control_frame, text="あなたの答え：", font=("メイリオ", 12))
answer_label.pack(side="left", padx=(20, 5))

# 答え入力欄
answer_entry = tk.Entry(control_frame, width=10, font=("メイリオ", 14))
answer_entry.pack(side="left")

# 答え合わせボタン（最初は無効にしておく）
check_button = tk.Button(
    control_frame, text="答え合わせ", font=("メイリオ", 12), command=check_answer
)
check_button.pack(side="left", padx=10)
check_button.config(state="disabled")

# 判定結果ラベル
result_label = tk.Label(root, text="", font=("メイリオ", 16))
result_label.pack(pady=10)

# メインループ開始
root.mainloop()
