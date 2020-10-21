info = ("张三", 18, 1.85)

# 格式化字符串后面的'()'本质上就是 元组
print("%s 的年龄是 %d，身高是%.3f" % info)

info_str = "%s 的年龄是 %d，身高是%.3f" % info

print(info_str)
