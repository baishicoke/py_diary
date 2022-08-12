import re
"""
自python 1.5 以后增加的re的模块，提供了正则表达式模式re模块使用了python语言拥有了全部表达式功能

re.match 函数
原型：match(pattern,string,flags=0)
pattern：匹配的正则表达式
string：需要匹配的字符串
flags：标志位，用于控制正则表达式的匹配方式，值如下
re.I 忽略大小写
re.L 做本地户识别
re.M 多行匹配，影响^和$
re.S 是匹配包括换行符在内的字符
re.U 根据Unicode字符集解析字符，影响 \w \W \b \B
re.X 使我们以更灵活的格式理解正则表达式
参数：
功能：尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话返回None

"""
print(re.match("www","www.baidu.com"))
print(re.match("www","www.baidu.com").span())
print(re.match("www","ww.baidu.com"))
print(re.match("www","wwW.baidu.com"))
print(re.match("www","wwW.baidu.com",flags=re.I))

"""
re.search函数
原型：search(pattern,string,flags=0)
pattern：匹配的正则表达式
string：需要匹配的字符串
flags：标志位，用于控制正则表达式的匹配方式

功能：扫描整个字符串，并返回第一个成功的匹配
"""
print(re.search("ajiu","good man is ajiu!ajiu is nice"))

"""
re.findall函数
原型：findall(pattern,string,flags=0)
pattern：匹配的正则表达式
string：需要匹配的字符串
flags：标志位，用于控制正则表达式的匹配方式

功能：扫描整个字符串，并返回结果列表
"""
print(re.findall("ajiu","good man is ajiu!Ajiu is nice",flags=re.I)[1])

