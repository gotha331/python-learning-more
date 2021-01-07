file = open("README.txt", encoding="utf-8")

while True:
    text = file.readline()

    # 判断是否读取到内容
    if not text:
        break
    print(text)

file.close()
