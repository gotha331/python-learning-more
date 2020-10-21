# 1.判断空白字符
space_str = "    \t\n\r"
print(space_str.isspace())

# 2. 判断字符串中是否只包含数字
#   >1 都不能判断小数
#   >2 isdecimal 判断全角数字
#      isdigit 可判断全角数字、①、\u00b2
#      isnumeric 可判断全角数字、汉字数字
num_str = "1"

print(num_str)
print(num_str.isdecimal())  # True
print(num_str.isdigit())  # True
print(num_str.isnumeric())  # True

num_str2 = "一二三"

print(num_str2)
print(num_str2.isdecimal())  # False
print(num_str2.isdigit())  # False
print(num_str2.isnumeric())  # True

num_str3 = "①"  # unicode字符串

print(num_str3)
print(num_str3.isdecimal())  # False
print(num_str3.isdigit())  # True
print(num_str3.isnumeric())  # True

num_str4 = "\u00b2"
print(num_str4)
print(num_str4.isdecimal())  # False
print(num_str4.isdigit())  # True
print(num_str4.isnumeric())  # True
