import cards_tools

while True:

    # 显示功能菜单
    cards_tools.show_menu()

    action_str = input("请选择操作功能：")
    print("您选择的操作是【%s】" % action_str)

    # 1,2,3 针对名片的操作
    if action_str in ["1", "2", "3"]:

        # 新增名片
        if action_str == "1":
            pass
        # 显示全部
        elif action_str == "2":
            pass
        # 查询名片
        else:
            # TODO(jiang) 查询名片功能
            pass

            # 0 退出系统
    elif action_str == "0":
        print("欢迎再次使用【名片管理系统】")
        break

    # 其他内容输入错误,需要提示用户
    else:
        print("您输入的不正确,请重新选择")
