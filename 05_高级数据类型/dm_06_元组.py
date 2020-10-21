# Tuple 元组与列表类似，不同之处在于元组的元素不能修改

info_tuple = ("zhangsan", 18, 1.75, 18)

print(type(info_tuple))
print("名字是 %s" % info_tuple[0])

single_tuple = (5,)

print(type(single_tuple))

# 取值和取索引
print(info_tuple[1])
print(info_tuple.index(1.75))

# 统计计数
print(info_tuple.count(18))
print(len(info_tuple))

# 循环遍历
for info in info_tuple:
    print(info)
