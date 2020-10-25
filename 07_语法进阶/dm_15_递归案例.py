# 需求：
# 1.定义一个函数sum_numbers
# 2.能够接受一个num的整数参数
# 3.计算1+2+3+...+num的结果

def sum_numbers(num):
    if num == 1:
        return 1

    # 假设 sum_numbers能够完成 num -1 的累加
    temp = sum_numbers(num - 1)

    # 函数内部的核心算法
    return num + temp


result = sum_numbers(6)
print(result)
