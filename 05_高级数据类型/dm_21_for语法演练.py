for num in [1, 2, 3]:
    print(num)

    if num == 2:
        break

else:
    # 当for循环完全执行完后，才会执行else部分
    # 当循环因break退出,else部分不会执行

    print("这里会执行吗")

print("循环结束")
