# 练习1： 定义一个整数变量age,编写diamagnetic判断年龄是否是正确，
# 要求人的年龄在0-120之间
age = int(input("请输入年龄："))

if 0 <= age <= 120:
    print('年龄合法')
else:
    print("非法的年龄，请核对")

# 练习2： 定义两个整数变量 python_scope,c_scope,编写代码判断成绩：
# 要求只要有一门成绩>60份就算合格

python_scope = int(input("请输入python成绩："))
c_scope = int(input("请输入c成绩："))

if python_scope > 60 or c_scope > 60:
    print("合格")
else:
    print("不合格")

# 练习3： 定义一个布尔类型变量is_employee,编写代码判断是否是本公司员工
# 如果不是，提示不允许入内
is_employee = False

if not is_employee:
    print("您的身份不合法，禁止入内")
