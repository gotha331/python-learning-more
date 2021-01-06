class MusicPlayer(object):
    # 记录第一个被创建对象的引用
    instance = None

    # 记录是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 1.判断类属性是否是空对象
        if cls.instance is None:
            # 2.调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3.返回类属性保存的对象引用
        return cls.instance

    def __init__(self):
        if self.init_flag:
            return
        else:
            print("初始化播放器")
            self.init_flag = True


# 创建多个对象
player1 = MusicPlayer()
print(player1)
print(MusicPlayer.instance)

player2 = MusicPlayer()
print(player2)
print(MusicPlayer.instance)
