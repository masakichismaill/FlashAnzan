import tkinter as tk
import random

root = tk.Tk()
root.title("フラッシュ暗算アプリ")
root.geometry("700x550")

# =============================
# 内部データ
# =============================
numbers = []
total_sum = 0
current_index = 0

# 統計
total_questions = 0  # 回数
correct_answers = 0  # 正答した回数
streak = 0  # 連続正解

# =============================
# 設定（桁数・問題数）
# =============================
digit_var = tk.StringVar(value="1")  # 1桁
count_var = tk.IntVar(value=5)  # 5問


# =============================
# フラッシュ暗算ロジック
# =============================
def start_flash():
    """問題生成してフラッシュ開始"""
    global numbers, total_sum, current_index

    digits = int(digit_var.get())  # 1or2or3
    min_val = 10 ** (digits - 1)  # １桁->1,２桁->10,３桁->100
    max_val = 10**digits - 1  # １桁->9,２桁->99,３桁->999

    num_count = count_var.get()

    numbers = [random.randint(min_val, max_val) for _ in range(num_count)]
    total_sum = sum(numbers)
    current_index = 0

    answer_entry.delete(0, tk.END)
    result_label.config(text="")
    # フラッシュ中ボタンを押せないようにする
    start_button.config(
        state="disabled"
    )  # disabled->今は使えないようにする。normal->普通に押せる
    check_button.config(state="disabled")

    show_next_number()


def show_next_number():
    """1秒ごとに次の数字を表示"""
    global current_index

    if current_index < len(numbers):
        number_label.config(text=str(numbers[current_index]))
        current_index += 1

        root.after(1000, show_next_number)  # 1000ミリ秒後にshow_next_numberを読んでね
    else:
        number_label.config(text="合計を入力してね")
        check_button.config(state="normal")
        start_button.config(state="normal")


def check_answer():
    """正誤判定"""
    global total_questions, correct_answers, streak

    user_text = answer_entry.get().strip()
    if not user_text:
        result_label.config(text="答えを入力してね")
        return

    try:
        user_answer = int(user_text)
    except ValueError:
        result_label.config(text="数字で入力してね")
        return

    total_questions += 1

    if user_answer == total_sum:
        correct_answers += 1
        streak += 1
        result_label.config(text=f"正解！ 合計は {total_sum}")
    else:
        streak = 0
        result_label.config(text=f"残念… 正解は {total_sum}")

    # 正答率の表示
    rate = (correct_answers / total_questions) * 100
    stats_label.config(text=f"正答率：{rate:.1f}%　連続正解：{streak}回")


# =============================
# UI：タイトル
# =============================
title_label = tk.Label(root, text="フラッシュ暗算", font=("メイリオ", 22, "bold"))
title_label.pack(pady=10)

# =============================
# UI：設定（桁数・問題数）
# =============================
settings_frame = tk.Frame(root)
settings_frame.pack(pady=10)

# 桁数
tk.Label(settings_frame, text="桁数：", font=("メイリオ", 12)).grid(row=0, column=0)
# Radiobuttonでは同じvariableを使うことで１つ選ぶと他が自動で外れる
tk.Radiobutton(settings_frame, text="1桁", value="1", variable=digit_var).grid(
    row=0, column=1
)
tk.Radiobutton(settings_frame, text="2桁", value="2", variable=digit_var).grid(
    row=0, column=2
)
tk.Radiobutton(settings_frame, text="3桁", value="3", variable=digit_var).grid(
    row=0, column=3
)

# 問題数
tk.Label(settings_frame, text="問題数：", font=("メイリオ", 12)).grid(
    row=1, column=0, pady=5
)
tk.Spinbox(settings_frame, from_=3, to=50, textvariable=count_var, width=5).grid(
    row=1, column=1
)

# =============================
# UI：フラッシュ数字
# =============================
number_label = tk.Label(root, text="準備OK？", font=("メイリオ", 40, "bold"))
number_label.pack(pady=20)

# =============================
# UI：答え入力
# =============================
control_frame = tk.Frame(root)
control_frame.pack(pady=10)

start_button = tk.Button(
    control_frame, text="スタート", font=("メイリオ", 14), command=start_flash
)
start_button.pack(side="left", padx=10)

tk.Label(control_frame, text="あなたの答え：", font=("メイリオ", 12)).pack(
    side="left", padx=5
)

answer_entry = tk.Entry(control_frame, width=10, font=("メイリオ", 14))
answer_entry.pack(side="left")

check_button = tk.Button(
    control_frame, text="答え合わせ", font=("メイリオ", 12), command=check_answer
)
check_button.pack(side="left", padx=10)
check_button.config(state="disabled")

# =============================
# UI：結果
# =============================
result_label = tk.Label(root, text="", font=("メイリオ", 16))
result_label.pack(pady=10)

stats_label = tk.Label(root, text="正答率：0%　連続正解：0回", font=("メイリオ", 14))
stats_label.pack(pady=5)

# =============================
# GO!
# =============================
root.mainloop()
