def demo(*args, **kwargs):
    print(args)
    print(kwargs)


# 元组变量/字典变量
gl_nums = (1, 2, 3)
gl_dict = {"name": '小明', "age": 18}

demo(gl_nums, gl_dict)

# 在调用带有多值参数的函数时，如果希望：
# 1.将一个元组变量直接传递给args
# 2.将一个字典变量直接传递给kwargs

# 就可以使用 拆包，简化参数的传递，拆包的方式是：
# 1.在元组变量前，增加一个*
# 2.在字典变量前，增加两个*
demo(*gl_nums, **gl_dict)
