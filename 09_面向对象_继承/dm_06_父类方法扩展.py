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

    # 方法扩展
    def bark(self):
        # 1.针对子类特有需求，编写代码
        print('神一样的叫唤。。。')

        # 2.使用super()调用原本在父类中封装的方法
        super().bark()

        # 3.增加其他子类的代码
        print('!@##$%&&&&&&*)_)(*&^%$')

wangcai = Dog()
wangcai.bark()

xtq = XiaoTianQuan()
xtq.bark()
