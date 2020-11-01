# 一个对象的 属性 可以是 另外一个类创建的对象


# 需求：
# 1.士兵 许三多 有一把 AK47
# 2.士兵可以开火
# 3.枪能够发射子弹
# 4.枪装填 装填子弹 -- 增加子弹数量


class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        # 1.判断子弹数量
        if self.bullet_count <= 0:
            print("[%s] 没有子弹了..." % self.model)
            return

        # 2.发射子弹
        self.bullet_count -= 1

        # 3.提示发射信息
        print("[%s] 突突突... 还剩余 [%d] 发子弹" % (self.model, self.bullet_count))


class Soldier:

    def __init__(self, name):
        self.name = name

        # 枪 - 新兵没有枪
        self.gun = None

    def fire(self):
        # 1.判断是否有枪
        # is 用于判断两个变量引用对象是否为同一个
        # == 用于判断引用变量的值是否相等
        if self.gun is None:
            print("[%s] 还没有枪" % self.name)

        # 2.高喊口号
        print("冲啊.....")

        # 3.让枪装填子弹
        self.gun.add_bullet(50)

        # 4.让枪发射子弹
        self.gun.shoot()


ak47 = Gun("AK47")

# ak47.add_bullet(100)
# ak47.shoot()

xusanduo = Soldier("许三多")
xusanduo.gun = ak47
print(xusanduo.gun)
# xusanduo.gun.shoot()

xusanduo.fire()
