action_list = ["新建名片", "显示全部", "查询名片"]


def show_menu():
    """显示菜单"""

    print("*" * 50)
    print("欢迎使用【名片管理系统】V1.0")
    print("")
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询名片")
    # for action_item in action_list:
    #     print("%d. %s" % (action_list.index(action_item) + 1, action_item))

    print("")
    print("0. 退出系统")
    print("*" * 50)
