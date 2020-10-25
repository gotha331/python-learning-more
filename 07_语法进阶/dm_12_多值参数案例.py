# 计算任意多个数字的和

def sum_numbers(*args):
    num = 0

    for n in args:
        num += n

    return num


result = sum_numbers(1, 2, 3, 4)
print(result)
  