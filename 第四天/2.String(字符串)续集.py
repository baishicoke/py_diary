"""
什么是字符串？
字符串是以单引号或双引号括起来的任意文本
'abc'
"def"
字符串不可变
"""
#创建字符串
str1 = "ajiu is a good man!"
str2 = "ajiu is a nice man!"
str3 = "ajiu is a handsome man!"
# ……
#字符串运行
str4 = "ajiu is a"
str5 = "good man"
str6 = str4 + str5
print(str6)
#输出重复字符串
str7 = "good"
str8 = str7 * 3
print("str8=",str8)

#访问字符串中的莫一个字符
#通过索引下标查找字符，索引从0开始
#字符串名[下标/索引]
str9 = "ajiu is a good man!阿九"
print(str9[1])

# str9[1] == "a" #字符串不可变
# print(str9)
# str10 = str9[1] == "a"  #并不能赋值
# print(str10)

#截取 字符串中的一部分
str11 = "ajiu is a good man!"
#从给定下标开始截取到给定下标之前
str12 = str11[5:9]
print(str12)

#从头截取到给定下标之前
str13 = str11[:5]
print(str13)

#从给定下标处开始截取到结尾
str14 = str11[10:]
print(str14)

#is 身份运算符  in 成员运算符

str15 = "ajiu is a good man"
print("good" in str15)
print("adfdsdd" in str15)

#格式化输出

print("ajiu is a good man")

num = 10
str16 = "ajiu is a nice man!"
f = 10.1236
print("num=",num,"str16=",str16)

# %d %s  %f   占位符
# %.3f 精确到小数点后3为，会四舍五入
print("num = %d,str16 = %s,f = %.3f"%(num,str16,f))

# 转义字符 \ 将一些字符转换成有特殊含义的字符
# \n #换行符
print("num = %d\nstr16 = %s\nf = %.3f"%(num,str16,f))
# \\
print("ajiu\\is")

# \' \"
print('tom is a \'good\'man')
print("tom is a \"good\"man")

print("tom is a 'good'man")
print('tom is a "good"man')

# 如果字符串中有好多字符串需要转义就需要加入好多\,为了简化,python允许用r表示内部的字符串默认不转义的
print(r'tom\is\a\good\man')
print("C:\\Users\\Administrator\\Desktop\\课件")
print(r"C:\Users\Administrator\Desktop\课件")

# \t 制表符 类似于四个空格，也就是一个Tab键的效果，它的作用是对齐表格数据的各列
print("ajiu\tgood")

# \\\t\\
print(r"\t")
print(r"\\\t\\")


#eval(str) 函数
#功能：将字符串str当成有效的表达式来求值返回结果（仅限：正数、浮点数、复数）不可在其中穿插其它字符字母等……
num1 = eval("123") #int
print(num1)
print(type(num1))
print(eval("+123"))
print(eval("-123"))

print(eval("12+3"))
# print(int("12+3"))
print(eval("12-3"))
# print(eval("a132"))
# print(eval("1a32"))
print(eval("3.123"))

#len(str) 返回字符串的长度（字符个数）从1开始
print(len("ajiu is good man!"))

#ord()函数 它是一个字符串(Unicode 字符)作为参数，返回对应的ASCII 数值（十进制）
str17 = "a"
print(ord(str17))

#chr() 函数 根据提供的ASCII 数值 返回相应字符串(Unicode 字符)。它的功能和ord()函数相反
print(chr(33))


####String.方法
#count(str[,start][,end]) 返回字符串中very出现的次数，可以指定一个范围，默认从头到尾
#str 要查找的字符
#start 开始的位，默认为0
#edn 结束的位置，默认为字符串的长度
str18 = "ajiu is a very very nice man"
print(str18.count("very",15,len(str18)))
print(str18.count("very"))

#find(str[,start][,end])
#str 要查找的字符
#start 开始的位，默认为0
#edn 结束的位置，默认为字符串的长度
#从左向右检测str字符串是否包含在字符串中,可以指定范围，默认从头到尾。得到的第一次出现的开始下标，没有返回-1
str19 = "ajiu is a very very nice man"
print(str19.find("very"))
print(str19.find("good"))
print(str19.find("very",15,len(str19)))

#rfind(str[,start][,end])
#str 要查找的字符
#start 开始的位，默认为0
#edn 结束的位置，默认为字符串的长度
#从右向左检测str字符串是否包含在字符串中,可以指定范围，默认从头到尾。得到的第一次出现的开始下标，没有返回-1
str20 = "ajiu is a very very nice man"
print(str20.rfind("very"))
print(str20.rfind("good"))
print(str20.rfind("very",15,len(str19)))

#index(str)
#str 要查找的字符
#start 开始的位，默认为0
#edn 结束的位置，默认为字符串的长度
#从左向右检测str字符串是否包含在字符串中，存在折返回下标 没有直接报错
str21 = "ajiu is a very very nice man"
print(str21.index("very"))
# print(str21.index("good"))

#rindex(str)
#str 要查找的字符
#start 开始的位，默认为0
#edn 结束的位置，默认为字符串的长度
#从右向左检测str字符串是否包含在字符串中，存在折返回下标 没有直接报错
str22 = "ajiu is a very very nice man"
print(str22.rindex("very"))
print(str22.rindex("very"))
# print(str22.rindex("good"))

#lstrip() 截掉字符串左侧指定的字符，默认为空格
str23 = "*******ajiu is a nice man****"
print(str23.lstrip("*"))
str24 = "       ajiu is a nice man****"
print(str24.lstrip())

#rstrip() 截掉字符串右侧指定的字符，默认为空格
str25 = "*******ajiu is a nice man****"
print(str25.rstrip("*"))
str26 = "       ajiu is a nice man****"
print(str26.rstrip())

#strip() 截掉字符串首尾指定的字符，默认为空格
str27 = "*******ajiu is a nice man    ****"
print(str27.strip("*"))
str28 = "       ajiu is a nice man     "
print(str28.strip())

str29 = "       ajiu is a nice man     *"
print(str29.strip())








