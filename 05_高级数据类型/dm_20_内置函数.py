t_str = "ksdjfggjksdhakjjhgjkshagahsdkahkladshlkashklas"

# 统计字符串中最大最小字符数
print(max(t_str))
print(min(t_str))

t_list = [5, 2, 4, 8, 1]
print(max(t_list))
print(min(t_list))

t_dict = {
    "a": "z",
    "b": "y",
    "c": "x"
}

# max/min 只会针对字典的key值进行比较
print(max(t_dict))
print(min(t_dict))

print("1" < "2")  # True
print("aaaa" < "bb")  # True
print([2, 2, 1] < [2, 2, 2])  # True
print((2, 2, 1) < (2, 2, 2))  # True

# 字典和字典不能比较大小
