import csv


time = ["20時", "21時", "22時"]

dayOfWeek = ["月", "火", "水", "木", "金", "土", "日"]

# ここからcsvファイルの中身を読み取る
contents_2D = []
contents_3D = []

numOfMember_2D = 0
numOfMember_3D = 0

Day_2D_A = [[0 for i in range(7)] for i in range(3)]
Day_2D_B = [[0 for i in range(7)] for i in range(3)]
Day_3D_A = [[0 for i in range(7)] for i in range(3)]
Day_3D_B = [[0 for i in range(7)] for i in range(3)]

Mem_2D_A = [[[] for i in range(7)] for i in range(3)]
Mem_2D_B = [[[] for i in range(7)] for i in range(3)]
Mem_3D_A = [[[] for i in range(7)] for i in range(3)]
Mem_3D_B = [[[] for i in range(7)] for i in range(3)]

with open("result.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    # csvファイルの中身を変数に格納しておく
    for row in reader:
        if "2D" in row[12]:
            numOfMember_2D += 1
            # 参加できない日を集計する
            for j in range(3):  # j = 20,21,22時で回すためのもの
                dekinai = row[3+j].split(", ")
                for k in range(len(dayOfWeek)):  # k = 曜日の数で回す
                    if dayOfWeek[k] in dekinai:
                        Day_2D_A[j][k] += 1
                        Mem_2D_A[j][k].append(row[1])
            # 参加したい日を集計する
            for j in range(3):  # j = 20,21,22時で回すためのもの
                shitai = row[6+j].split(", ")
                for k in range(len(dayOfWeek)):  # k = 曜日の数で回す
                    if dayOfWeek[k] in shitai:
                        Day_2D_B[j][k] += 1
                        Mem_2D_B[j][k].append(row[1])
            contents_2D.append(row)
        if "3D" in row[12]:
            numOfMember_3D += 1
            # 参加できない日を集計する
            for j in range(3):  # j = 20,21,22時で回すためのもの
                dekinai = row[3+j].split(", ")
                for k in range(len(dayOfWeek)):  # k = 曜日の数で回す
                    if dayOfWeek[k] in dekinai:
                        Day_3D_A[j][k] += 1
                        Mem_3D_A[j][k].append(row[1])
            # 参加したい日を集計する
            for j in range(3):  # j = 20,21,22時で回すためのもの
                shitai = row[6+j].split(", ")
                for k in range(len(dayOfWeek)):  # k = 曜日の数で回す
                    if dayOfWeek[k] in shitai:
                        Day_3D_B[j][k] += 1
                        Mem_3D_B[j][k].append(row[1])
            contents_3D.append(row)

message = "2D(can,月,火,水,木,金,土,日,,2D(want,月,火,水,木,金,土,日,,3D(can,月,火,水,木,金,土,日,,3D(want,月,火,水,木,金,土,日\n"
message += f"20時,{Day_2D_A[0][0]},{Day_2D_A[0][1]},{Day_2D_A[0][2]},{Day_2D_A[0][3]},{Day_2D_A[0][4]},{Day_2D_A[0][5]},{Day_2D_A[0][6]},,20時,{Day_2D_B[0][0]},{Day_2D_B[0][1]},{Day_2D_B[0][2]},{Day_2D_B[0][3]},{Day_2D_B[0][4]},{Day_2D_B[0][5]},{Day_2D_B[0][6]},,20時,{Day_3D_A[0][0]},{Day_3D_A[0][1]},{Day_3D_A[0][2]},{Day_3D_A[0][3]},{Day_3D_A[0][4]},{Day_3D_A[0][5]},{Day_3D_A[0][6]},,20時,{Day_3D_B[0][0]},{Day_3D_B[0][1]},{Day_3D_B[0][2]},{Day_3D_B[0][3]},{Day_3D_B[0][4]},{Day_3D_B[0][5]},{Day_3D_B[0][6]}\n"
message += f"21時,{Day_2D_A[1][0]},{Day_2D_A[1][1]},{Day_2D_A[1][2]},{Day_2D_A[1][3]},{Day_2D_A[1][4]},{Day_2D_A[1][5]},{Day_2D_A[1][6]},,21時,{Day_2D_B[1][0]},{Day_2D_B[1][1]},{Day_2D_B[1][2]},{Day_2D_B[1][3]},{Day_2D_B[1][4]},{Day_2D_B[1][5]},{Day_2D_B[1][6]},,21時,{Day_3D_A[1][0]},{Day_3D_A[1][1]},{Day_3D_A[1][2]},{Day_3D_A[1][3]},{Day_3D_A[1][4]},{Day_3D_A[1][5]},{Day_3D_A[1][6]},,21時,{Day_3D_B[1][0]},{Day_3D_B[1][1]},{Day_3D_B[1][2]},{Day_3D_B[1][3]},{Day_3D_B[1][4]},{Day_3D_B[1][5]},{Day_3D_B[1][6]}\n"
message += f"22時,{Day_2D_A[2][0]},{Day_2D_A[2][1]},{Day_2D_A[2][2]},{Day_2D_A[2][3]},{Day_2D_A[2][4]},{Day_2D_A[2][5]},{Day_2D_A[2][6]},,22時,{Day_2D_B[2][0]},{Day_2D_B[2][1]},{Day_2D_B[2][2]},{Day_2D_B[2][3]},{Day_2D_B[2][4]},{Day_2D_B[2][5]},{Day_2D_B[2][6]},,22時,{Day_3D_A[2][0]},{Day_3D_A[2][1]},{Day_3D_A[2][2]},{Day_3D_A[2][3]},{Day_3D_A[2][4]},{Day_3D_A[2][5]},{Day_3D_A[2][6]},,22時,{Day_3D_B[2][0]},{Day_3D_B[2][1]},{Day_3D_B[2][2]},{Day_3D_B[2][3]},{Day_3D_B[2][4]},{Day_3D_B[2][5]},{Day_3D_B[2][6]}\n"

tmp = ""

for i in range(3):
    tmp = ""
    tmp += ","
    for j in range(7):
        tmp += "\""
        for k in range(len(Mem_2D_A[i][j])):
            tmp += f"{Mem_2D_A[i][j][k]}\n"
        tmp += "\","
    tmp += ",,"
    for j in range(7):
        tmp += "\""
        for k in range(len(Mem_2D_B[i][j])):
            tmp += f"{Mem_2D_B[i][j][k]}\n"
        tmp += "\","
    tmp += ",,"
    for j in range(7):
        tmp += "\""
        for k in range(len(Mem_3D_A[i][j])):
            tmp += f"{Mem_3D_A[i][j][k]}\n"
        tmp += "\","
    tmp += ",,"
    for j in range(7):
        tmp += "\""
        for k in range(len(Mem_3D_B[i][j])):
            tmp += f"{Mem_3D_B[i][j][k]}\n"
        tmp += "\","
    message += f"{tmp}\n"

print(Mem_3D_A)

print(message)
with open("result_cg.csv", mode="w") as f:
    f.write(message)
