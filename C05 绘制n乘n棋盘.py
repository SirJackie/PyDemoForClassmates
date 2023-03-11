# 创建棋盘
qiPan = []
for y in range(0, 3):
    yiHangQiPan = []
    for x in range(0, 3):
        yiHangQiPan.append(0)
    qiPan.append(yiHangQiPan)


# 绘制棋盘
def Draw(yourQiPan):
    for y in range(0, 3):
        for x in range(0, 3):
            print(yourQiPan[y][x], end="")
        print("\n", end="")


Draw(qiPan)
