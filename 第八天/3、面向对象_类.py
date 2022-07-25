"""
面向对象 类
栈的数据结构实现
在类（class） 里面 def 叫方法  类似于：string。方法还有list方法
"""
class Stack:
    def __init__(self):   #在类初始化执行的第一个函数
        self.stack = []
    def append(self,value):
        self.stack.append(value)
    def pop(self):
        return self.stack.pop()
    def lenGth(self):
        return len(self.stack)
    def getTop(self):
        if self.lenGth()!=0:
            return self.stack[-1] #返回最后一个元素
        return None
    def getStack(self):
        return self.stack    #这样我们可以看见它还剩下那些元素在里面


if __name__ == '__main__':
    s = Stack()
    for i in range(1,3):
        print(i)
        s.append(i)
    # print(s.getTop())
    # print(s.lenGth())
    # print(s.pop())
    print(s.getStack())
    