
# print(3/0)
# 需求：当程序遇到问题时不让程序结束，而越过错误继续向下执行

"""
try......except......else
格式：
try:
    语句t
except 错误码 as e：
    语句n
else:
    语句e
注意:else语句可有可无
作用：用来检测语句块中的错误，从而让except语句捕获错误信息并处理
逻辑：当程序执行到try......except......else语句时
当try ”语句t“ 执行出现错误；会匹配到一个错误码如果匹配上就执行对应的语句
"""
try:
    print(3/0)

except ZeroDivisionError as e:
    print("除数为零")
else:
    print("代码没有问题")