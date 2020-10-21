poem = ["\t\n登鹳雀楼",
        "王之涣",
        "白日依山尽\n",
        "黄河入海流\t",
        "欲穷千里目",
        "\n更上一层楼"]

for poem_str in poem:
    # 先使用strip方法去除字符串中左右两边的空白字符
    # 再使用center方法居中显示文本

    # print("|%s|" % poem_str)
    print("|%s|" % poem_str.strip().center(10, "　"))
