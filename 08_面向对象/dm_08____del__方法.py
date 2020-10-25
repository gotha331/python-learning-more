class Cat:

    def __init__(self, new_name):
        self.name = new_name

        print("%s 来了" % self.name)

    def __del__(self):
        print("%s 走了" % self.name)


tom = Cat("Tom")
print(tom.name)
print("-" * 50)

# tom 是一个全局变量，当所有代码执行完毕后，才会对其进行内存回收，执行__del__方法
