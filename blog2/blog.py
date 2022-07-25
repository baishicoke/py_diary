"""
这是程序启动的地方
"""

import os

import menu
import service

if __name__ == "__main__":
    # 记录日志
    service.record("程序启动。。。。。")

    # 记录日志
    service.record("从数据文件blog.dat中加载系统数据")
    # 初始化数据
    service.load_file()

    # 展示登陆菜单
    service.record("展示登录菜单")

    menu.show_login()
