import csv

# csvファイルの説明(変更用)
# 列の要素名
# 2:部門、3:できない20時、4:できない21時、5:できない22時、6:質問、7:したい20時、8:したい21時、9:したい22時
#
#
# できるだけ短くて複雑なコードを書いてみました！（）


# ★★★部門が増えたらここを増やしてね！★★★
departments = ["CG部", "PROG部", "DTM部", "MV部"]

contents = []

dayOfWeek = ["月", "火", "水", "木", "金", "土", "日"]
# 参加できない日を記録する
# 月,火,水,木,金,土,日
# [[0, 0, 0, 0, 0, 0, 0],  20時
# [0, 0, 0, 0, 0, 0, 0],   21時
# [0, 0, 0, 0, 0, 0, 0]]   22時
#
#
A = [[[0 for k in range(7)] for j in range(3)]
     for i in range(len(departments))]
# 参加したい日を記録する
B = [[[0 for k in range(7)] for j in range(3)]
     for i in range(len(departments))]

# 質問があれば記録する
question = []

# 投票したメンバーの数を記録
numOfMember = 0

# 投票したメンバーの数(部門ごと)を記録
numOfDepMenber = [0 for i in range(len(departments))]

with open("result.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    # csvファイルの中身を変数に格納しておく
    for row in reader:
        contents.append(row)

    for i in range(len(departments)):  # i = 部門の数で回す
        for member in contents:  # member= 部員で行を回す
            if "タイムスタンプ" == member[0]:
                continue
            if departments[i] in member[2]:  # 〇〇部所属？かで絞る
                # ここまでで、それぞれの部門のメンバーを絞りました。
                numOfDepMenber[i] += 1
                # 参加できない日を集計する
                for j in range(3):  # j = 20,21,22時で回すためのもの
                    dekinai = member[3+j].split(", ")
                    for k in range(len(dayOfWeek)):  # k = 曜日の数で回す
                        if dayOfWeek[k] in dekinai:
                            A[i][j][k] += 1
                # 参加したい日を集計する
                for j in range(3):  # j = 20,21,22時で回すためのもの
                    shitai = member[7+j].split(", ")
                    for k in range(len(dayOfWeek)):  # k = 曜日の数で回す
                        if dayOfWeek[k] in shitai:
                            B[i][j][k] += 1

    # 質問があれば記録する
    for member in contents:
        if member[0] == "タイムスタンプ":
            continue
        numOfMember += 1  # 投票総数記録用
        if not (member[6] == ""):
            question.append(member[6])

    # 集計終わり

# 表示する文章を構成する。
message = f"\n\
【2023年度前期 曜日決めアンケート集計結果】\n\
今回の活動日決めアンケートの結果を表示します。\n\
\n\
投票総数：{numOfMember}\n\
--------------------------------------------------\n"

for i in range(len(departments)):
    pass


print(message)
