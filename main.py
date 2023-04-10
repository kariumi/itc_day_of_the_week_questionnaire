import csv

# csvファイルの説明(変更用)
# 列の要素名
# 2:部門、3:できない20時、4:できない21時、5:できない22時、6:質問、7:したい20時、8:したい21時、9:したい22時
#
#
#


# ★★★部門が増えたらここを増やしてね！★★★
departments = ["CG部", "PROG部", "DTM部", "MV部"]


message = "今回の活動日決めアンケートの結果を表示します。\n--------------------------------------------------\n"

contents = []

dayOfWeek = ["月", "火", "水", "木", "金", "土", "日"]
# 参加できない日を記録する
A = [[[0 for k in range(7)] for j in range(3)]
     for i in range(len(departments))]
# 参加したい日を記録する
B = [[[0 for k in range(7)] for j in range(3)]
     for i in range(len(departments))]

with open("result.csv", encoding="utf-8") as f:

    reader = csv.reader(f)

    # csvファイルの中身を変数に格納しておく
    for row in reader:
        contents.append(row)

    for i in range(len(departments)):
        print(f"【{departments[i]}志望の人】")
        for row in contents:
            if not ("タイムスタンプ" == row[0]):
                if departments[i] in row[2]:
                    # ここまでで、それぞれの部門のメンバーを絞りました。

                    print(row[1])
