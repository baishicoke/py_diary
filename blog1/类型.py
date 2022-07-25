"""
创建第一个类型
"""


# 通过class关键字，创建一个新的自定义类型数据
class Person:
    # 在一个特殊函数中定义类型的属性
    def __init__(self):
        self.name = "李明"
        self.age = 18
        self.gender = "男"
        self.height = 177
        self.weight = 88

    # 定义类型的行为(就是函数，在面向对象中函数被称为方法)
    def eat(self, food):
        print("%s吃饭了，吃的是%s" % (self.name, food))


# 创建第一个对象
p1 = Person()
# 对象的属性
print(p1.name, p1.age, p1.weight, p1.height, p1.gender)
# 操作对象的方法
p1.eat("鱼香肉丝")

p2 = Person()
