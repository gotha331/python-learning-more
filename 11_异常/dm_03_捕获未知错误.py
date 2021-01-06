try:
    # 提示用户输入一个整数
    num = int(input("请输入一个整数:"))

    # 使用8除以用户输入的整数并输出
    result = 8 / num
    print(result)

except ValueError:
    print("请输入正确的整数")

except Exception as result1:
    print("未知错误 %s" % result1)
