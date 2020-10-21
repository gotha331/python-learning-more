hello_str = "hello world"

# 1.判断字符串是否以指定字符开始
print(hello_str.startswith("hell"))

# 2.判断字符串是否以指定字符结束
print(hello_str.endswith("rld"))

# 3.查找指定字符串
# index 如果指定的字符串不存在，会报错
# find 如果指定的字符串不存在，会返回-1
print(hello_str.find("ll"))
print(hello_str.find("abc"))

# 4.替换字符串
# replace 返回新的字符串，原字符串保持不变

print(hello_str.replace("h", "H"))
print(hello_str)
