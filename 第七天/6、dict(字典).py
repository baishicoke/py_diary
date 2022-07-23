'''
概述:
使用 键-值（key-value）存储，具有极快的查找速度
注意：字典是无序的
Key的特性：
1、字典中的key必须唯一
2、key必须是不可变对象
3、字符串、整数等都是不可变的，可以作为key
4、list 是可变的，不能作为key

思考：保存多为学生的姓名成绩，使用字典，学生姓名为key,学生成绩作为值
'''
#创建字典
# dict1 = {}
# print(type(dict1))

dict1 = {"tom":60,"lilei":70}

#元素的访问
#获取值：通过 字典名[key] 返回 值
print(dict1["lilei"])
# print(dict1["ajiu"])
print(dict1.get("ajiu"))
ret = dict1.get("ajiu")
if ret == None:
    print("没用")
else:
    print("有")
# 添加
dict1["ajiu"] = 99
print(dict1)
#因为一个key对应一个value，所以，可以多次对一个key的值赋值，其实就是修改值
#改变
dict1["lilei"] = 88
print(dict1)

#删除
dict1.pop("tom")
print(dict1)

#查找   注意无论有没有key 控号必须为中括号[]  否者一律报错
# dict1("lilei")
# print(dict1)



#遍历
for key in dict1:
    print(key,dict1[key])
#取出字典中的所有值
print(dict1.values())
for value in dict1.values():
    print(value)
#返回字典中所有 的key和值
print(dict1.items())

for k,v in dict1.items():
    print(k,v)

#enumerate(iterable[,start]) 获得索引和key
#iterable
#start 默认是0
for i,v2 in enumerate(dict1):
    print(i,v2)

#取出字典中的所有键
print(dict1.keys())

#清空字典
# dict1.clear()
# print(dict1)
print("dict1：",dict1)
dict2 = dict1.copy()
print("dict2：",dict2)

#字典和list比较
#1、查找和插入的数度极快，不会随着key-value的增加而变慢
#2、需要占用大量的内存，内存浪费多

#list
#1、查找和插入的速度随着数据量的增多而减慢
#2、占用空间小，浪费内存少








