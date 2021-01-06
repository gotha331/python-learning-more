class Dog(object):

    # 静态方法
    @staticmethod
    def run():
        # 当方法内部不访问实例属性/类属性时，可以将方法定义为静态方法
        print('小狗要跑...')


# 通过类名.调用静态方法 - 不需要创建对象
Dog.run()
