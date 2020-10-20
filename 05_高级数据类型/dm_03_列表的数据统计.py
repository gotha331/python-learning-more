name_list = ["张三", "李四", "王五", "李四"]

# len (length 长度) 函数可以统计列表中元素的总数
list_len = len(name_list)
print("列表中包含%d个元素" % list_len)

# count 方法可以统计列表中某一个数据出现的次数

str_count = name_list.count("李四")
print("\"李四\"出现的次数是%d次" % str_count)
