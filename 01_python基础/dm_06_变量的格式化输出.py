# %s 字符串
# %d 有符号十进制整数，%06d 表示输出的整数显示位数，不足的地方使用0补全
# %f 浮点数，%.02f 表示小数点后只显示两位
# %% 输出%

# 1.定义字符串变量 name，输出 我的名字叫小明，请多多关照！

name = '小明'
print("我的名字叫 %s,请多多关照" % name)

# 2.定义整数变量 student_no，输出我的学号是000001
student_no = 1
print("我的学号是%06d" % student_no)

# 3.定义小数 price、weight、money，输出 苹果单价9.00元/斤，购买了5.00斤，需要支付45.00元
price = 5
weight = 9
money = price * weight
print("苹果单价 %.2f 元/斤，购买了 %.2f 斤，需要支付 %.2f 元" % (price, weight, money))

# 4.定义一个小数scale，输出 数据比例是10.000%
# scale = 10
# print("数据比例是 %.3f%%" % scale)

scale = 0.25
print("数据比例是 %.2f%%" % (scale * 100))
