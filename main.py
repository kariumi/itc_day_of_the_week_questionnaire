import csv
import pprint

# 【お知らせ】
# 部門が減ったり増えたりしてもこのプログラムを使用することができます。部門名をdepartmentsリストに追加、削除してください。


# 【デバッグ用】
# csvファイルの説明(変更用)
# 列の要素名
# 2:部門、3:できない20時、4:できない21時、5:できない22時、6:したい20時、7:したい21時、8:したい22時、9:質問
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

# 最もみんな参加できる日のminAを記録
minAList = []

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
                    shitai = member[6+j].split(", ")
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


# 最も多くの部員が参加できる日を記録する
dekinai = [[]for m in range(len(departments))]
kouho = [[]for m in range(len(departments))]

section = 1
message = f"\n\
【2023年度前期 曜日決めアンケート集計結果】\n\
【序論】\n\
今回の活動日決めアンケートの結果を表示します。\n\
\n\
【集計方法】\n\
① 参加できない日のアンケートから最も多くの人が参加できる日を割り出します。= 集合A\n\
② 集合Aの要素が一つならばそれを部会日とします。複数なら③へ進みます\n\
③ 参加したいのアンケートから、集合Aの中で最も多くの人が参加したい日を割り出します。 = 集合B\n\
④ 集合Bの要素数が1なら、それを部会日とし、複数ならそれらを部会日の候補とします。\n\
\n\
投票総数：{numOfMember}\n\n\
    - ---------------------------------------------------------------------------------------------------\n"


for i in range(len(departments)):
    message += f"\
【{departments[i]}】\n\n\
・投票総数：{numOfDepMenber[i]}\n\n"

    minA = min(min(A[i], key=min))
    minAList.append(minA)
    maxB = max(max(B[i], key=max))
    tmp = ""

    # 参加できない日を集める 20時：0~6,21時：7~13,22時：14~20
    for j in range(len(A[i])):
        tmp += f"{time[j]}\t|"
        for k in range(len(A[i][j])):
            tmp += f"\t{A[i][j][k]}"
            if A[i][j][k] == minA:
                dekinai[i].append([j*7+k, 0])
        tmp += f"\n    "

    # 参加できない日のアンケ結果を表示

    message += f"\
    ❌参加できない日の投票結果を表示します。（最小値:{minA}）\n\
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

    kouho = dekinai

    # みんなが参加できる日の、参加したい人数を記録
    for n in range(len(dekinai[i])):
        youbi = dekinai[i][n][0] % 7
        times = int(dekinai[i][n][0] / 7)
        kouho[i][n][1] = B[i][times][youbi]

    # 参加したい日のアンケ結果を表示

    message += f"\
    ⭕参加したい日の投票結果を表示します。（最大値:{maxB}）\n\
    時間帯\t|\t月\t火\t水\t木\t金\t土\t日\n\
    {tmp}\n"
    message += "----------------------------------------------------------------------------------------------------\n"


# アンケ結果表示終了

# アンケ結果から候補日を決定する処理↓
# kouhoリストに全部入っている。

# まずは参加したい人の数でリストをソート
sorted_kouho = []
for i in range(len(departments)):
    sorted_kouho.append(sorted(kouho[i], key=lambda x: x[1], reverse=True))

sorted_kouho2 = sorted_kouho
message += f"⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐\n最も最良な候補日は、\n\n"
maxBList = []

for i in range(len(departments)):
    # sorted_kouhoの参加したい人の最大値を出す
    maxBList.append(sorted_kouho[i][0][1])

    message += f"⭐ {departments[i]}⭐ (参加できない：{minAList[i]}人、参加したい{maxBList[i]}人)\n"

    for j in sorted_kouho[i]:
        if j[1] == maxBList[i]:
            youbi = j[0] % 7
            times = int(j[0]/7)
            message += f"- {dayOfWeek[youbi]}{time[times]}\n"
    message += f"\n"

message += f"です。\n\n"
message += f"上の候補が被っている場合は更に下の候補を参考にしてください。↓↓\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n"
message += f"参加できない人が最も少ない候補をおすすめ順に並べると、(括弧内の数字は参加したい人の数)\n\n"

for i in range(len(departments)):
    message += f"🟦 {departments[i]}🟦 (参加できない：{minAList[i]}人)\n"
    for j in sorted_kouho[i]:
        youbi = j[0] % 7
        times = int(j[0]/7)
        message += f"- {dayOfWeek[youbi]}{time[times]}（{j[1]}）\n"

    message += "\n"


message += f"です。\n"
message += f"ここから選択できない場合は、上のアンケ結果を参考に決めてください。\n"

# saiteki = []
# if len(dekinai) == 1:
#     i = int(dekinai[0]/7)
#     j = dekinai[0] % 7
#     saiteki.append(f"【{dayOfWeek[j]}{time[i]}】\n")
# else:
#     for day in dekinai:
#         if day in shitai:
#             i = int(day/7)
#             j = day % 7
#             saiteki.append(f"{dayOfWeek[j]}{time[i]}")
# tmp = ""
# if len(saiteki) == 1:  # 最もみんなが参加できる日が一つに絞られた場合
#     tmp = f"部会に最適な日が一つに絞られました。以下のとおりです。この日に部会に参加できない人は{minA}人、この日に参加したい人は{maxB}人です。\n"
# else:
#     tmp += f"部会に最適な日が複数ありました。以下のとおりです。なお、この日に部会に参加できない人は{minA}人、この日に参加したい人は{maxB}人です。\n"

# message += f"{tmp}\n⭐"
# for day in saiteki:
#     message += f"{day}⭐、⭐"
# message = message.rstrip("、⭐")
# message += "⭐\n\n"


# ここから、質問一覧

message += f"----------------------------------------------------------------------------------------------------\n【寄せられた質問一覧】\n"

for q in range(len(question)):
    message += f"{1+q}. {question[q]}\n"


print(message)


with open("result.txt", mode="w", encoding='UTF-8') as f:
    f.write(message)
