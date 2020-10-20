name_list = ["zhangsan", "lisi", "wangwu"]

# 1.取值和取索引
print(name_list[0])

print(name_list.index("lisi"))

# 2. 修改
name_list[1] = "李四"
print(name_list)

# 3. 增加
# append 方法可以向列表的末尾追加数据
name_list.append("王小二")

# insert 方法可以在列表的指定索引位置插入数据
name_list.insert(1, "王钢蛋")
print(name_list)

# extend 方法可以爸其他列表中的完整内容，追加到当前列表的末尾
temp_list = ["于鬻菊", "诸葛钢针", "阿依土鳖公主"]
name_list.extend(temp_list)
print(name_list)

# 4. 删除

# remove 方法可以从列表中删除指定的数据
name_list.remove("zhangsan")
print(name_list)

# pop 方法默认可以把列表中最后一个元素删除
name_list.pop()
print(name_list)

# pop 方法可以指定要删除元素的索引
name_list.pop(2)
print(name_list)

# clear 方法可以清空列表
name_list.clear()
print(name_list)
