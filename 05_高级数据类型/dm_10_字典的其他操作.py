student_dict = {
    "name": "小明",
    "age": 18,
    "gender": "male"
}

# # 常用操作
# print(list(student_dict.keys()))
# print(list(student_dict.values()))
# print(list(student_dict.items()))

#  1. 统计键值对数量
print(len(student_dict))

#  2. 合并字典
temp_dict = {
    "height": 1.75,
    "age": 20
}

student_dict.update(temp_dict)

print(student_dict)

#  3. 清空字典
student_dict.clear()
print(student_dict)
