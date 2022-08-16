import re

#字符串切割
str1 = "ajiu     is a good man"
print(str1.split(" "))
print(re.split(" ",str1))
print(re.split(r" +",str1))
"""
re.finditer 函数
原型：finditer(pattern,string,flags=0)
参数：
pattern：匹配的正则表达式
string：需要匹配的字符串
flags：标志位，用于控制正则表达式的匹配方式
功能：与findall类似，扫描整个字符串，返回的是一个迭代器
"""
str2 = "ajiu is a good man! ajiu is a nice man! ajiu is a very handsome man"
d = re.finditer(r"(ajiu)",str2)
while True:
    try:
        l = next(d)
        print(d)
    except StopIteration as e:
        break
"""
字符串的替换和修改
sub(pattern,repl,string,count=0)
subn(pattern,repl,string,count=0)
pattern：匹配的正则表达式
repl：指定的用来替换的字符串
string：目标字符串
count：最多替换次数
功能：在目标字符串中以正则表达式的规则匹配字符串，再把他们替换成指定的字符串。
可以指定替换的次数,如果不指定，替换所有的匹配字符串
区别：前者返回一个被替换的字符串，后者返回一个元组，第一个元素被替换的字符串，第二个元素表示被替换的次数
"""
str3 = "ajiu is a good good good man"
# print(re.sub(r"(good)","nice",str3))
print(type(re.sub(r"(good)","nice",str3)))
print(re.subn(r"(good)","nice",str3))

"""
分组
概念：除了简单的判断是否匹配之外，正则表达式还有提取子串的功能。用()表示的就是提取分组
"""
str4 = "010-53248754"
m = re.match(r"(?P<first>\d{3})-(?P<last>\d{8})",str4)
#使用序号获取对应组的信息，group(0)一直代表的原始字符串
print(m.group(0)) #返回全部
print(m.group(1)) #返回前面的
print(m.group("first"))#返回前面的
print(m.group(2))#返回后面的
print(m.group("last"))#返回后面的
#查看匹配的各组情况
print(m.group())#返回全部

"""
编译：当我们使用正则表达式时，re模块会干两件事
1、编译正则表达式，如果正则表达式本身不合法，会报错
2、用编译后的正则表达式去匹配对象
compile(pattern,flags=0)
pattern：匹配的正则表达式
"""
pat = r"^1(([3578]\d|(47))\d{8})$"
print(re.match(pat,"13600000000"))
