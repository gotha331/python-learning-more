# 私有属性/私有方法 只希望在对象内部使用，而不希望在外部被访问到
# 在定义属性/方法时,在属性名/方法名前增加两个下划线，定义的就是私有属性或者方法


class Women:

    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        # 在对象的方法内部，是可以访问对象的私有属性的
        print("%s 的 年龄是 %d" % (self.name, self.__age))


douya = Women("豆芽")

print(douya.name)
# 私有属性在外部不能够被直接访问
# print(douya.__age)

# 私有方法，同样不允许在外界直接访问
# douya.__secret()

print(douya._Women__age)
douya._Women__secret()
