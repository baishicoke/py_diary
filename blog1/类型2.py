"""
功能：某个人给宠物喂食
1.分析出现的对象
2.分析对象的特征和行为
3.编程操作
"""


# 定义一个人的类型
class Person:
    def __init__(self, name, gender, pet):
        self.name = name
        self.gender = gender
        self.pet = pet

    # 定义人的行为
    def wei_shi(self, food):
        # 人喂食行为
        print("小乖乖，过来吃饭了。。。。")
        self.pet.eat(food)


class Pet:

    # 定义宠物特征
    def __init__(self, nickname):
        self.nickname = nickname

    def eat(self, food):
        print("宠物%s吃东西了，吃的是%s" % (self.nickname, food))


if __name__ == "__main__":
    # 创建具体对象：宠物
    cat = Pet("tom猫")

    # 创建具体对象人
    person = Person("李明", "女", cat)

    # 喂食操作
    person.wei_shi("面包")
