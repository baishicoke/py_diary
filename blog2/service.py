"""
业务数据处理模块
"""
import datetime
import os.path
import pickle
import sys
import time

import data


def login():
    u_username = input("请输入账号：")
    u_password = input("请输入密码：")
    record("用户输入了账号%s和密码%s" % (u_username, u_password))

    # 进行登录判断
    if u_username in data.users:
        # 判断密码是否正确
        if u_password == data.users.get(u_username).get("password"):
            # 登录成功记录当前登录用户
            record("用户输入了账号%s" % u_username)
            data.login = data.users.get(u_username)
            return True
        else:
            record("用户%s登录失败，账号或者密码有误" % u_username)

            input("账号或者密码有误，按任意键重新操作")
            return False
    else:
        record("用户%s登录失败，账号或者密码有误" % u_username)
        input("没有这个用户，按任意键继续")
        return False


def regist():
    record("用户开始注册新账号")

    # 提示用户输入数据
    u_username = input("请输入注册账号：")
    if u_username in data.users:
        record("用户%s注册失败，用户账号已经存在")
        input("账号已存在，请使用其他账号进行注册")
        return

    u_password = input("请输入密码：")
    u_nickname = input("请输入昵称：")

    # 构建一个简单的用户字典
    record("用户信息正确正在注册")

    user = {"username": u_username, "password": u_password, "nickname": u_nickname}

    # 添加到系统数据模块中
    record("用户数据正在保存到系统中")

    data.users[u_username] = user
    save_file()
    record("用户%s信息保存完成" % (u_username))
    input("注册完成，按任意加继续")
    return True


def load_file():
    """
    从文件中读取项目数据
    :return:
    """
    # # 打开一个储存数据的系统文件
    # f = open("blog.dat", "rb")
    #
    # # 读取数据
    # data.users = pickle.load(f)
    if os.path.exists("blog.dat"):
        with open("blog.dat", "rb") as f:
            data.users = pickle.load(f)

    if os.path.exists("article.dat"):
        with open("article.dat", "rb") as f:
            data.articles = pickle.load(f)


def save_file():
    """
    向文件保存数据
    :return:
    """
    # # 打开一个储存数据的系统文件
    # f = open("blog.dat", "wb")
    # # 保存数据到文件中
    # pickle.dump(data.users, f)
    #
    # # 关闭文件
    # f.close()
    # with语句是简化的文件操作语法；开始执行时自动打开文件，with中的代码执行完毕自动关闭文件
    with open("blog.dat", "wb") as f:
        pickle.dump(data.users, f)

    with open("article.dat", "wb") as f:
        pickle.dump(data.articles, f)


def publish_article():
    # 提示用户输入文章信息
    record("用户开始发表文章 ")
    title = input("请输入文章标题：")
    content = input("请输入文章内容")
    author = data.login.get("username")
    publish = get_current_time()

    # 包装一个文章字典
    record("用户%s准备发表，文章标题：%s" % (data.login.get("username"), title))
    article = {"title": title, "publish": publish, "author": author, "content": content}

    # 储存到系统数据模块中
    data.articles.append(article)
    return True


def exit_system():
    print("程序将在3s后退出,正在保存数据")
    # 调用系统函数
    time.sleep(1)
    print("程序将在2s后退出,正在保存数据")
    time.sleep(1)
    print("程序将在1s后退出,正在保存数据")
    time.sleep(1)
    save_file()
    print("程序成功退出")
    sys.exit(1)


def record(msg):
    """
    记录日志的函数，记录消息msg
    :param msg:
    :return:
    """
    with open("blog.log", "a", encoding="UTF-8") as f:
        f.write(get_current_time() + ":" + msg + "\r\n")


def get_current_time():
    """
    获取当前系统时间
    :return:
    """
    t = datetime.datetime.now()
    return "%s年%s月%s日 %s:%s:%s" % (t.year, t.month, t.day, t.hour, t.minute, t.second)
