# 计算0-100之间所有偶数的累计求和结果

i = 0
result = 0

while i <= 100:
    if i % 2 == 0:
        result += i
    i += 1

print("0-100之间的偶数求和结果是：%d" % result)
