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
        # 1.针对子类特有的需求，编写代码
        print("呜呼～～～汪汪")

        # 2.使用super(). 调用原本在父类中封装的方法
        super().bark()

        # 3.增加其他子类的代码
        print("$%^$%^$%^$%^")


xiaotianquan = XiaoTianQun()

xiaotianquan.fly()
xiaotianquan.bark()
xiaotianquan.sleep()
xiaotianquan.run()
xiaotianquan.drink()
xiaotianquan.eat()


