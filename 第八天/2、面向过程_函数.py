"""
面向过程 函数
参数传递
返回
"""
def add(a:int,b:int):
    return a+b

def bdd():
    #强制转换数字
    a,b = input(">>>").split(" ")
    print("a is %d, b is %d" %(int(a),int(b)))
    return add(int(a),int(b))

if __name__ == '__main__':
    # result = add(1,3)
    # print(result)
    result = bdd()
    print(result)
    








