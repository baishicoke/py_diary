import pickle #数据持久性模块
myList = [1,2,3,4,5,"sjdkl"]

#写出
path = r"C:\Users\Administrator\Desktop\课件\第十天\file4.txt"
with open(path,"wb") as f1:
    pickle.dump(myList,f1)

#读取
with open(path,"rb") as f2:
    tempList = pickle.load(f2)
    print(tempList)
