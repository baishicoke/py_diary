path = r"C:\Users\Administrator\Desktop\课件\第十天\file3.txt"
#写出 并编码
with open(path,"wb") as f1:
    str1 = "ajiu is a good man帅"
    f1.write(str1.encode("utf-8"))
#读出 解码
with open(path,"rb") as f2:
    data = f2.read()
    print(data)
    print(type(data))
    newData = data.decode("utf-8")
    print(newData)
    print(type(newData))








