# 需求1：定义一个print_line函数，能够打印*组成的一条分隔綫
def print_line():
    print("*" * 50)


# 需求2：定义一个函数能够打印由任意字符组成的分隔綫
def print_line_02(char):
    print(char * 50)


# 需求3： 定义一个函数能够打印任意重复次数的任意字符的分隔綫
def print_line_03(char, times):
    print(char * times)


print_line()
print_line_02("+")
print_line_03("-", 51)
