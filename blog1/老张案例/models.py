"""
定义类型的模块
"""


class Person:
    """
    人的类型
    """

    def __init__(self, name):
        self.name = name

    def driver(self, car, address):
        print("老张乘[%s]车出发了。。。" % car.name)
        car.run(address)


class Car:
    """
    车的类型
    """

    def __init__(self, name):
        self.name = name

    def run(self, address):
        print("驶向%s" % address.name)


class Address:
    """
    目的地
    """

    def __init__(self, name):
        self.name = name
