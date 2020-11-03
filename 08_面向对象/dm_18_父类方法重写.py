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


class XiaoTianQun(Dog):
    def fly(self):
        print("我会飞")

    # 方法重写，会覆盖父类中定义的方法
    def bark(self):
        print("呜呼～～～汪汪")


xiaotianquan = XiaoTianQun()

xiaotianquan.fly()
xiaotianquan.bark()
xiaotianquan.sleep()
xiaotianquan.run()
xiaotianquan.drink()
xiaotianquan.eat()
