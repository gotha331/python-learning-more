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


class   XiaoTianQuan(Dog):
    def fly(self):
        print("神狗起飞")


class Cat(Animal):
    def catch(self):
        print("我会抓老鼠")

wangcai = Dog()

wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()

print('-------------xtq--------------')
xtq = XiaoTianQuan()
xtq.eat()
xtq.drink()
xtq.run()
xtq.sleep()
xtq.bark()
xtq.fly()

# xtq不能调用Cat的catch方法

