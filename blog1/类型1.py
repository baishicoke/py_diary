"""
定义一个类型
"""


class Person:
    """
    创建一个人的类型
    """

    def __init__(self, name, age, gender):
        """
        根据传入人的参数，初始化人的参数
        :param name:名称
        :param age:年龄
        :param gender:性别
        """
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self, food):
        """
        定义一个人的行为
        :param food: 要吃的食物
        :return: 无
        """
        print("%s要吃饭了，%s" % (self.name, food))


# 创建一个对象：对象就是某一个类型实际存在的一个个体
p1 = Person("李明", 18, "男")  # 语法中自动调用init参数
print(p1.name, p1.age, p1.gender)
p1.eat("烤全羊")

p2 = Person("小红", 17, "女")
print(p2.name, p2.age, p2.gender)
p2.eat("烤全羊")

