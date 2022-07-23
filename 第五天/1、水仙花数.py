# 第三天作业 三位数水仙花数 讲解
num = int(input("请输入一个三位数："))
# 153 370 371 407
a = num % 10
b = num // 10 % 10
c = num // 100
# a**3 a的3次方  pow(c,3) c的3次方
if num == a**3 + b**3 + c**3:
    print("yes")
else:
    print("no")
