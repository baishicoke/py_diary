"""
程序启动入口
"""
import models

if __name__ == "__main__":
    # 创建对象
    zhang = models.Person("老张")

    # 创建车和地址对象
    bao_ma = models.Car("宝马")
    dong_bei = models.Address("东北")

    # 老张开车去东北
    zhang.driver(bao_ma,dong_bei)


