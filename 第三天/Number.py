import math,random

#分类：整数、浮点数、复数

#整数：pyrhon可以处理任意大小的整数，当然包括复整数，在程序中的表示和数学的写发一样

num1 = 10
num2 = num1
print(num2)
#连续定义多个变量
num3 = num4 = num5 = 1
print(num3,num4,num5)
#交互式赋值定义变量
num6,num7 = 6,7
print(num6,num7)

#浮点数：浮点数由整数部分与小数部分分组成，浮点数运算可能会有四舍五入的误差。

f1 = 1.1
f2 = 2.2
f3 = f1 + f2
print(f3)

#复数
num8 = -123
print(num8)

#数字类型转换

print(int(1.9))
print(float(1))
print(int("123"))
print(float("12.3"))
#如果有其它无用字符会报错
# print(int("abc"))
# print(int("55666abc"))
#只有作为正负号才有意义
print(int(+123))
print(int("+123"))
print(int(-123))
print(int("-123"))
#print(int("12+3"))

#返回数字的绝对值
a1 = -10
a2 = abs(a1)
print(a2)

#比较两个数的大小
a3 = 100
a4 = 9
#True
print(a3>a4)
#False
print(a3<a4)

print((a3>a4)-(a3<a4))
#返回给定参数的最大值
print(max(1,2,3,4,5,6,7,8,9))
#返回给定参数的最小值
print(min(1,2,3,4,5,6,7,8,9))

#向上取整
print(math.ceil(18.1))
print(math.ceil(18.9))
#向下取整
print(math.floor(18.1))
print(math.floor(18.9))

#随机数
#从序列的元素中随机挑选一个元素
print(random.choice([1,3,5,7,9]))
print(random.choice(range(5)))#range(5)==[0,1,2,3,4]
print(random.choice("ajiu"))#"ajiu"==[a,j,i,u]
#生产一个1~100之间的随机数
r1 = random.choice(range(100))+1
print(r1)

#random.randrange([start,]stop[,step])
#start--指定范围的开始值，包含在范围内，默认0
#stop--指定范围的结束值，不包含在范围内
#step--指定的递增基数，默认是1
print(random.randrange(1,100,2))
#从0-99选取一个随机数
print(random.randrange(100))

#随机生成0-1之间的浮点数
print(random.random())

list1 = [1,2,3,4,5]
#将序列的所有元素随机排序
random.shuffle(list1)
print(list1)

#生随机产一个实数，他在3-9范围的浮点数
print(random.uniform(3,9))



