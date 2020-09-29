"""
if的嵌套演练-火车站安检
需求
    1.定义布尔型变量has_ticket表示是否有车票
    2.定义整型变量knife_length表示刀的长度，单位：厘米
    3.首先检查是否有车票，如果有，才允许进行安检
    4.安检时，需要检查刀的长度，判断是否超过20厘米
        ・如果超过20厘米，提示刀的长度，不允许上车
        ・如果不超过20厘米，安检通过
    5.如果没有车票，不允许进门
"""

has_ticket = True
knife_length = 30

if has_ticket:
    print("车票检车通过，准备安检")

    if knife_length < 20:
        print("安检通过，请上车")
    else:
        print("您携带的刀太长了，有%d厘米长，禁止乘车" % knife_length)
else:
    print("请购票后，进行安检")
