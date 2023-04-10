import csv

# 【お知らせ】
# 部門が減ったり増えたりしてもこのプログラムを使用することができます。部門名をdepartmentsリストに追加、削除してください。


# 【デバッグ用】
# csvファイルの説明(変更用)
# 列の要素名
# 2:部門、3:できない20時、4:できない21時、5:できない22時、6:質問、7:したい20時、8:したい21時、9:したい22時
#
#


# ★★★部門が増えたらここを増やしてね！★★★
departments = ["CG部", "PROG部", "DTM部", "MV部"]

contents = []

time = ["20時", "21時", "22時"]

dayOfWeek = ["月", "火", "水", "木", "金", "土", "日"]
# 参加できない日を記録する
# 月, 火,水, 木,金, 土,日
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
section = 1
message = f"\n\
【2023年度前期 曜日決めアンケート集計結果】\n\
{section}. 序論\n\
今回の活動日決めアンケートの結果を表示します。\n\
\n\
投票総数：{numOfMember}\n\
--------------------------------------------------\n"
section += 1

for i in range(len(departments)):
    message += f"\
{section}. {departments[i]}の投票結果\n\
・投票総数：{numOfDepMenber[i]}\n"
    minA = min(min(A[i], key=max))
    maxB = max(max(B[i], key=max))
    tmp = ""

    # 参加できない日を集める 20時：0~6,21時：7~13,22時：14~20
    dekinai = []
    for j in range(len(A[i])):
        tmp += f"{time[j]}\t|"
        for k in range(len(A[i][j])):
            tmp += f"\t{A[i][j][k]}"
            if A[i][j][k] == minA:
                dekinai.append(j*7+k)
        tmp += f"\n    "

    # 参加できない日のアンケ結果を表示

    message += f"\
    ❌参加できない日の投票結果を表示します。\n\
    時間帯\t|\t月\t火\t水\t木\t金\t土\t日\n\
    {tmp}\n"
    tmp = ""

    # 参加できない日アンケによる結論
    # tmp = "【参加できない日アンケによる結論】\n"
    # if minA == 0:
    #     if len(dekinai) == 1:
    #         tmp += "全員が参加できる日が一つに絞られました！以下の通りです。"
    #     else:
    #         tmp += "全員が参加できる日は複数ありますが、以下の通りです。"
    # else:
    #     tmp = f"全員が参加できる日はありませんでした。"
    #     if len(dekinai) == 1:
    #         tmp += "しかし、最も投票数が少ない日は一つに絞られました。以下の通りです。"

    #     else:
    #         tmp += f"最も投票数が少ない日を以下の通りです。なお、この日は{minA}人が参加できないと投票しています。"

    # message += f"   {tmp}\n"
    # tmp = ""
    # for day in dekinai:
    #     i = int(day/7)
    #     j = day % 7
    #     tmp += f"{dayOfWeek[j]}{time[i]}、"
    # tmp = tmp.rstrip("、")
    # message += f"   {tmp}\n\n"
    # tmp = ""

    # 参加したい日を決める
    shitai = []
    for j in range(len(B[i])):
        tmp += f"{time[j]}\t|"
        for k in range(len(B[i][j])):
            tmp += f"\t{B[i][j][k]}"
            if B[i][j][k] == maxB:
                shitai.append(j*7+k)
        tmp += f"\n    "

    # 参加したい日のアンケ結果を表示

    message += f"\
    ⭕参加したい日の投票結果を表示します。\n\
    時間帯\t|\t月\t火\t水\t木\t金\t土\t日\n\
    {tmp}\n\
【{departments[i]}の総評】\n"

    saiteki = []
    if len(dekinai) == 1:
        i = int(day/7)
        j = day % 7
        saiteki.append(f"【{dayOfWeek[j]}{time[i]}】\n")
    else:
        for day in dekinai:
            if day in shitai:
                i = int(day/7)
                j = day % 7
                saiteki.append(f"{dayOfWeek[j]}{time[i]}")
    tmp = ""
    if len(saiteki) == 1:  # 最もみんなが参加できる日が一つに絞られた場合
        tmp = f"部会に最適な日が一つに絞られました。以下のとおりです。この日に部会に参加できない人は{minA}人、この日に参加したい人は{maxB}人です。\n"
    else:
        tmp += f"部会に最適な日が複数ありました。以下のとおりです。なお、この日に部会に参加できない人は{minA}人、この日に参加したい人は{maxB}人です。\n"

    message += f"{tmp}\n⭐"
    for day in saiteki:
        message += f"{day}⭐、⭐"
    message = message.rstrip("、⭐")
    message += "⭐\n"

    message += "--------------------------------------------------\n"
    section += 1

print(message)
