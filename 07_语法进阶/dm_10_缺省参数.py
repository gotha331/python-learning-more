def print_info(name, title="", gender=True):
    """
    打印姓名信息
    :param title: 职位
    :param name: 同学姓名
    :param gender: True 男生 False 女生
    :return:
    """

    gender_text = "男生"
    if not gender:
        gender_text = "女生"

    print("【%s】%s是%s" % (title, name, gender_text))


# 假设同学中-男生居多！
# 提示：在指定缺省参数的默认值时，应该使用最常见的值作为默认值！
# 缺省参数因该在参数的最末尾


print_info("刘翠花")
print_info("袁晓黄")
print_info("王钢蛋", gender=False)
