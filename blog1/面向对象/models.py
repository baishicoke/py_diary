"""
定义程序中可能出现各种类型
"""


class Person:
    def __init__(self, name, gender, friend):
        """
        定义初始化数据的函数：该函数在创建对象时会自动调用
        :param self: 
        :param name: 
        :param gender:
        :return: 
        """
        self.name = name
        self.gender = gender
        self.friend = friend

    def watch_movie(self, cinema, movie):
        """
        看电影的行为：可以去一个电影院cinema看一部电影
        :param cinema:
        :param movie:
        :return:
        """
        print("和%s开心地去看电影了...." % self.friend.name)
        # 电影院放映指定的电影
        cinema.show(movie)


class Cinema:
    """
    定义一个电影院类型
    """

    def __init__(self, name):
        """
        电影的属性
        :param name: 放映的电影
        """
        self.name = name

    def show(self, movie):
        """
        电影院放电影的行为
        :param movie:放映的电影
        :return:无
        """
        print("[%s]电影开始播放了" % movie.name)


class Movie:
    """
    电影类型
    """

    def __init__(self, name):
        """
        初始化电影名称
        :param name:
        """
        self.name = name
