
path = r"C:\Users\Administrator\Desktop\课件\第十天\file2.txt"
#ignore 忽略错误
f = open(path,"a")
#写文件
#1、将信息写入缓冲区
f.write("ajiu")
#2、刷新缓冲区
#直接把内部缓冲区的数据立刻写入文件，而不是被动的等待自动刷新缓冲区写入
f.flush()
#3、关闭文件
f.close()

with open(path,"a") as f2:
    f2.write("good man")
