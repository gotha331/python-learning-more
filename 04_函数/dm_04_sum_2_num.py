# 实现两个数字的求和


def sum_2_num(num1, num2):
    """
    两个数字求和
    :param num1: 
    :param num2: 
    :return: 
    """
    result = num1 + num2
    print("%d + %d = %d" % (num1, num2, result))
    return result


sum_result = sum_2_num(1, 3)
print("计算的结果是:%d" % sum_result)
