# 继承的概念：子类拥有父类的所有属性和方法


class Animal:

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


# Dog 类 从Animal类 继承/派生
class Dog(Animal):

    def bark(self):
        print("汪汪叫")


wangcai = Dog()

wangcai.bark()
wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
