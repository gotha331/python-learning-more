# 1.打开
file_read = open("README.txt", encoding="utf-8")
file_write = open("README[复件].txt", "w", encoding="utf-8")

# 2.读、写（逐行）
while True:

    # 读取一行内容
    text = file_read.readline()

    # 判断是否读取到内容
    if not text:
        break

    file_write.write(text)

# 3.关闭
file_read.close()
file_write.close()
