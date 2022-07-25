"""
定义程序中需要的个各种界面模块
"""
import data
import service


def show_login():
    print("\t\t系统用户登录")
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*")
    print("\t\t1.用户登录")
    print("\t\t2.用户注册")
    print("\t\t3.退出系统")
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*")

    choice = input("请输入选项：")
    service.record("用户开始访问，输入选项：%s" % choice)

    if choice == "1":
        service.record("开始用户登录")
        res = service.login()
        if res:
            service.record("用户登录成功")

            # 登陆成功展示首页
            show_index()
        else:
            # 登陆失败，重新展示首页
            show_login()
    elif choice == "2":
        service.record("用户开始注册")

        # 用户注册
        service.regist()
        # 返回登录页面
        show_login()
    elif choice == "3":
        service.record("用户%s退出了程序" % data.login.get("username"))
        service.exit_system()
    else:
        input("没有这个选项，按任意键退出")
        show_login()


def show_index():
    print("\t\t系统首页")
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*")
    print("\t\t1.维护个人信息")
    print("\t\t2.个人文章管理")
    print("\t\t3.返回登陆菜单")
    print("\t\t4.退出系统")
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*")
    choice = input("请输入您的选项：")
    service.record("用户开始访问，输入选项：%s" % choice)

    if choice == "1":
        pass
    elif choice == "2":
        show_article_manager()
    elif choice == "3":
        pass
    elif choice == "4":
        service.exit_system()
    else:
        input("没有这个选项按任意键继续")
        show_index()


def show_article_manager():
    """
    个人文章管理菜单
    :return:
    """
    print("\t\t菜单文件管理")
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
    print("\t\t1.发表文章")
    print("\t\t2.查看所有文章")
    print("\t\t3.返回上一级")
    print("\t\t4.退出系统")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    choice = input("请输入您的选项：")
    if choice == "1":
        # 发表文章
        service.publish_article()
        # 发表文章完成展示文章管理菜单
        show_article_manager()
    elif choice == "2":
        # 查看当前用户所有文章
        show_article_info(data.articles)
    elif choice == "3":
        pass
    elif choice == "4":
        service.exit_system()
    else:
        input("没有这个选项，按任意键返回文章管理")
        show_article_manager()


def show_article_info(articles):
    """
    打印展示所有文章数据
    :param articles:
    :return:
    """
    for a in articles:
        print("文章标题:%s" % a.get("title"))
        print("文章作者:%s" % a.get("author"))
        print("发布时间:%s" % a.get("publish"))
        print("~!~!~!~!~!~!~!~!~!~!~!~!~!~!")
    input("按任意键返回")
    show_article_manager()
