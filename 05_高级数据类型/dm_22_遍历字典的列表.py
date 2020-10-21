students = [
    {
        "name": "王钢蛋"
    },
    {
        "name": "诸葛钢针"
    }
]

# 在学员列表中搜索指定的姓名
# find_name = "王钢蛋"
find_name = "于谦的父亲王老爷子"

for stu_dict in students:
    # print(stu_dict)

    if stu_dict["name"] == find_name:
        print("找到了 %s" % find_name)
        break

else:
    print("找了一大圈，也没找到你要的人呢")

print("循环结束")
