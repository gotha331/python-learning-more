# 从控制台输入要出的拳 - 石头（1）/ 剪刀（2） / 布（3）
# 电脑 随机 出拳
# 比较胜负

import random

player = int(input("请输入您要出的拳-石头（1）/ 剪刀（2） / 布（3）:"))
computer = random.randint(1, 3)
print("玩家选择的拳头是：%d,电脑出的拳头是%d" % (player, computer))

if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("欧耶，电脑弱爆了")
elif player == computer:
    print("哈哈，打平了")
else:
    print("咦，玩家弱爆了")
