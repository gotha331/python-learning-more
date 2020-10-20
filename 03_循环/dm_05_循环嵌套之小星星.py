# 在控制台连续输出5行*，每一行*的数量依次递增

# row = 1
#
# while row <= 5:
#     row += 1
#     print('*' * row)


# 在默认情况下，print函数输出内容之后，会自动在内容末尾添加换行

# print("*", end="")
# print("*")


row = 1

while row <= 5:
    col = 1

    while col <= row:
        print("*", end="")
        col += 1
    # 这行代码的目的是在一行打印完成后，换行
    print("")
    row += 1
