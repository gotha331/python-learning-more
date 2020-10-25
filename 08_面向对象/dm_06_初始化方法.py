class Cat:

    # __init__方法是专门用来定义一个类具有哪些属性的方法！
    def __init__(self):
        print("这是一个初始化方法")


# 使用类名()创建对象的时候，会自动调用初始化方法__init__
tom = Cat()
