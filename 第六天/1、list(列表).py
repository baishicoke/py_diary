#思考：要存储5个人的年龄，求他们的平均年龄
age1 = 18
age2 = 19
age3 = 20
age4 = 21
age5 = 22
print((age1+age2+age3+age4+age5) / 5)

#使用list（列表）简化
#列表本质：是一种有序的集合
"""
创建列表
格式：列表名 = [列表选项1,列表选项1,……,列表选项n]
"""
#创建一个空列表
list1 = []
print(list1)
#创建带有元素的列表
list2 = [18,19,20,21,22]
index = 0
sum = 0
#嵌套最好不要超过3层
while index < 5:  #len(list2)
    sum += list2[index]
    index += 1
    if index == 5: #len(list2)
        print("平局年龄：%d" %(sum/5))

#注意：列表中的元素数据可以是不同类型的
list3 = [1,2,"ajiu","good",True]
print(list3)

#列表元素的访问  注意不要越界（下标超出了可以表示的范围）
#取值 格式：列表吗[下标]
list4 = [1,2,3,4,5]
print(list4[2])

#替换
list4[2] = 300
print(list4)

#列表操作：
#列表组合
list5 = [1,2,3]
list6 = [4,5,6]
list7 = list5 + list6
print(list7)
#列表的重复
list8 = [1,2,3]
print(list8 * 3)

list9 = [1,2,3,4,5]
print(3 in list9)
print(6 in list9)

#列表截取
list10 = [1,2,3,4,5,6,7,8,9]
print(list10[2:6])
print(list10[3:])
print(list10[:5])

#二维列表(列表嵌套)
list11 = [[1,2,3],[4,5,6],[7,8,9]]
print(list11[1][1])

#列表方法
#append 在列表中 末尾添加新的元素
list12 = [1,2,3,4,5]
list12.append(6)
list12.append([7,8,9])
print(list12)

#extend 在末尾一次性追加别一个列表中的多个值
list13 = [1,2,3,4,5]
list13.extend([6,7,8,9])
print(list13)

#在下标处添加一个元素，不覆盖原数据，原数据向后顺延
list14 = [1,2,3,4,5]
list14.insert(2,100)
print(list14)

#pop 移除列表中指定下标处的元素（默认移除最后一个元素），并返回删除的数据
list15 = [1,2,3,4,5]
list15.pop()
print(list15)
list15.pop(2)
print(list15)

#remove 移除列表中的某个元素第一个匹配的结果（从左往右的）
list16 = [1,2,3,4,5,4,5,4]
list16.remove(4)
print(list16)

#clear 清除列表中的所有数据
list17 = [1,2,3,4,5]
list17.clear()
print(list17)

#从列表中找出某个值 第一个匹配的索引值（从左往右的）
list18 = [1,2,3,4,5,3,4,5,6]
index18 = list18.index(3)
print(index18)
#圈定范围
index19 = list18.index(3,3,7)
print(index19)

#len 返回列表中元素的个数（从1开始）
list19 = [1,2,3,4,5,3,4,5,6]
print(len(list19))

#获取列表中的最大值
list20 = [1,2,3,4,9]
print(max(list20))

#获取列表中的最小值
list21 = [1,2,3,4,9]
print(min(list21))

#查看元素在列表中出现的次数
list22 = [1,2,3,4,5,3,4,5,6,3,3,3]
print(list22.count(3))
num23 = 0
all = list22.count(3)
while num23 < all:
    list22.remove(3)
    num23 += 1
print(list22)


#倒叙
list23 = [1,2,3,4,5]
list23.reverse()
print(list23)

#升序 （从小到大的）排序
list24 = [2,1,3,5,4]
list24.sort()
print(list24)

#将元组转成列表
list25 = list((1,2,3,4))
print(list25)







