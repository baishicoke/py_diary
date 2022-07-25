"""
程序运行的入口
"""
import models

if __name__ == "__main__":
    # 创建对象
    # 小红对象
    xh = models.Person("小红", "女", None)
    # 李明对象
    lm = models.Person("李明", "男", xh)
    # 创建电影院
    c = models.Cinema("万达影城")
    m = models.Movie("寻梦环游记")

    # 创建电影院
    lm.watch_movie(c, m)
