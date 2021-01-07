# 1.打开文件
file = open("README.txt", encoding='utf-8')

# 2.读取文件内容
text = file.read()
print(text)
print(len(text))

print("-" * 50)

# 读取文件后，文件指针会移动到文件末尾，导致读取不到内容
text = file.read()
print(text)
print(len(text))

# 3.关闭文件
file.close()
