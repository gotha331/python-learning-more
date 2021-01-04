# 私有属性和私有方法 是对象的隐私，不对外公开，外界及子类都不能直接访问
# 私有属性和私有方法 通常用于做一些内部的事情


class A:

    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def hah(self):
        print("我是A的公有方法 %d" % self.__num2)

        self.__test()

    def __test(self):
        print("我是A的私有方法%d %d" % (self.num1, self.__num2))


class B(A):

    def demo(self):
        # 1. 访问父类的公有属性
        print("子类方法调用父类的公有属性%d" % self.num1)

        # 2. 调用父类的公有方法
        self.hah()


# 创建一个子类对象
b = B()

# 在外界访问父类的公有属性和方法
print(b.num1)
b.hah()

b.demo()
