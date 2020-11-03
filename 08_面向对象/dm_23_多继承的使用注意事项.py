class A:

    def test(self):
        print("A --- test方法")

    def demo(self):
        print("A --- demo方法")


class B:

    def test(self):
        print("B --- test方法")

    def demo(self):
        print("B --- demo方法")


class C(B, A):
    """
    多继承可以让子类对象同时具有多个父类的属性和方法
    """
    pass


c = C()

c.test()
c.demo()


# 确定C类对象的调用顺序
print(C.__mro__)
