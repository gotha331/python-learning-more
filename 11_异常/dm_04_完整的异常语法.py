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

else:
    # 没有异常时，才会执行
    print("程序执行没有异常")

finally:
    # 不管有没有异常，最终都会执行
    print("程序执行完了")
