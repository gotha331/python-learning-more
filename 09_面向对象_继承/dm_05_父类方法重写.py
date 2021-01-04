# 如果父类的方法不能满足子类的需求时，可以对方法进行重写（override）
class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


# Dog继承Animal
class Dog(Animal):
    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):
    def fly(self):
        print("神狗起飞")

    # 父类的bark方法不能满足子类需求（完全不同），则方法进行重写（覆盖）
    def bark(self):
        print("神狗汪汪叫叫")


wangcai = Dog()
wangcai.bark()

xtq = XiaoTianQuan()
xtq.bark()
