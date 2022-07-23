#作用：跳出for和while循环
# 注意：只能跳出距离他最近的那一层循环
# for i in range(10):
#     print(i)
#     if i == 5:
#         #结束这个循环
#         break
# print("aaaaaaaaaaaa")
# a = 100
# while 1:
#     for i in range(10):
#         print(i)
#         if i == 5:
#             # 结束这个循环
#             break
#     print("嗨嗨嗨")
#
# print("BBBBBBBBBBBB")

# 注意：循环语句可以有else语句，break导致循环截止，不会执行else下面的语句
num = 1
while num <= 10:
    print(num)
    if num == 3:
        break
    num += 1
else:
    print("elseelseelseelse")
print("嗨嗨嗨")

