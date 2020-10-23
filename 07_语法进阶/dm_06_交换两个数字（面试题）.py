# 要求：
# 1.有两个变量 a = 6,b = 10
# 2.不使用其他变量，交换两个变量的值

a = 6
b = 10

# 解法1：使用其他变量
# c = a
# a = b
# b = c
#
# print(a)
# print(b)

# 解法2：不使用其他变量
# a = a + b
# b = a - b
# a = a - b
#
# print(a)
# print(b)

# 解法3：python专属，元组
# (a, b) = (b, a)
# 提示：等号右边是一个元组，只是把小括号省略了

a, b = b, a
print(a)
print(b)
