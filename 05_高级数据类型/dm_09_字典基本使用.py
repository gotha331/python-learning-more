student_dict = {
    "name": "小明",
    "age": 18,
    "gender": "male"
}

print(student_dict)

# 1.取值
print(student_dict['name'])

# 2.增加/修改
student_dict['height'] = 1.75
student_dict['name'] = "small 明"
print(student_dict)

# 3.删除
student_dict.pop('gender')

print(student_dict)

