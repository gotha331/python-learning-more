# 假设：以下内容是从网络上抓取的
# 要求：顺序并且居中对齐输出以下内容
poem = ["登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]

for poem_str in poem:
    print("|%s|" % poem_str.center(10, "　"))  # 添加全角中文空格

print('*' * 50)

for poem_str in poem:
    print("|%s|" % poem_str.ljust(10, "　"))  # 添加全角中文空格

print('*' * 50)

for poem_str in poem:
    print("|%s|" % poem_str.rjust(10, "　"))  # 添加全角中文空格
