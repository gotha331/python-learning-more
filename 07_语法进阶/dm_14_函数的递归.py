# 递归函数：函数内部自己调用自己

def sum_numbers(num):
    print(num)

    # 递归的出口，当参数满足某个条件时，不再执行函数
    # 很重要，否则函数将会无限循环执行下去
    if num == 1:
        return

    sum_numbers(num - 1)


sum_numbers(5)
