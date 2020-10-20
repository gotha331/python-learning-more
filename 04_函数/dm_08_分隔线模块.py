def print_line(char, times):
    print(char * times)


def print_lines(char, times, num):
    """打印多条分隔线

    :param char:打印样式
    :param times:每一行的字符数
    :param num:需要打印的行数
    :return:
    """
    while num > 0:
        print_line(char, times)
        num -= 1


name = "升官发财，名利双收"

# print_lines("*", 60, 5)
