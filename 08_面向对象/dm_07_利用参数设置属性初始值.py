class Cat:

    def __init__(self, new_name):
        print("这是一个初始化方法")

        # 定义用Cat类创建的猫对象都有一个name的属性

        self.name = new_name

    def eat(self):
        print("%s 爱吃鱼" % self.name)


# 使用类名()创建对象的时候，会自动调用初始化方法__init__
tom = Cat('Tom')

tom.eat()

lazy_tom = Cat("大懒猫")
lazy_tom.eat()
