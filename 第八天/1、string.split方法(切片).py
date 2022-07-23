"""
str.split(sep[,maxsplit])
str:表示要分割的字符串
sep：用于指定分割符，可以包含多个字符。此参数默认为 None 表示所以空字符。包括空格、换行符 “\n” 制表符 “\t”等。
| 13211   &&&&&
#maxsplit：可选参数，用于指定分割的次数，最后列表中字串的个数最多为 maxsplit+1. 如果不指定分割的次数，则表示分割次数没有限制。有多少全部都会分割
"""
str = "张三 >>> 李四"

#采用默认分割符进行分割
list1 = str.split()
print(list1)

#采用多个字符进行分割
list2 = str.split(">>>")
print(list2)

#采用空格进行分割，并规定最多能分割成4个子串
str2 = "张三 李四 张三 李四 张三 李四 张三 李四"
list3 = str2.split(" ",4)
print(list3)

list4 = str.split(">")#采用>字符进行分割
print(list4)
#张三
#
#
#  李四

str = "张三 李四 张三 李四 张三 李四 张三 李四"
list2 = str.split(" ",3)
print(list2)





