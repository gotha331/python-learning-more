i = 0

while i < 10:
    # break 某一条件满足时，退出循环，不再执行后续重复的代码
    # continue 某一条件满足时，跳出循环，不再执行后续代码，重新进入循环体

    # i==3

    i += 1

    if i == 8:
        break

    if i == 4:
        continue

    print(i)
