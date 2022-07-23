str1 = "hello&&world&&ajiu"
print(str1.split("&&"))
#字符串链接合并
print(" ".join(str1.split("&&")))

#在字符串开头结尾做文本匹配
# Str.startswith()  #开头
# Str.endswith()   #结尾
str2 = ["test.py","hello.cpp","鱼刺.e","socket.erl"]
for s in str2:
    if s.endswith("刺.e"):
        print(s)

#字符串多次替换
intab = "aeiou" #用作替换的字符
outtab = "12345" #要替换的字符
trantab = str.maketrans(intab,outtab)
str4 = "this is string example....wow!!!"
print(str4.translate(trantab))

#字符串单次替换
print(str4.replace("i","1"))
print(str4.replace("i","1").replace("e","2"))  #可以拼接多个

num = 10
str16 = "ajiu is a nice man!"
f = 10.1236
print("num=",num,"str16=",str16)

# %d %s  %f  %r  占位符
# %d 数字
# %s 字符串
# %.3f 精确到小数点后3为，会四舍五入
# %r 原封不动的替换 就像是骡子就是骡子 马儿就是马儿
print("num = %d,str16 = %s,f = %.3f, r = %r"%(num,str16,f,str16))

name = "ajiu"
age = 20
str5 = "name:{}; age:{}".format(name,age)
print(str5)


name = "ajiu"
age = 20
str6 = f"name:{name}; age:{age}"
print(str6)



