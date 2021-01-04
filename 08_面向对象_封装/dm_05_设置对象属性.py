class Cat:

    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print("%s爱吃鱼" % self.name)

    def drink(self):
        print("%s要喝水" % self.name)


# 创建猫对象
tom = Cat()

# 可以使用 .属性名 设置对象属性（不推荐 ）
tom.name = "Tom"

print(tom)

tom.eat()
tom.drink()

# 再创建一个猫对象
lazy_cat = Cat()
print(lazy_cat)
lazy_cat.name = "大懒猫"

lazy_cat.eat()
lazy_cat.drink()

lazy_cat2 = lazy_cat
print(lazy_cat2)
