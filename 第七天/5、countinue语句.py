'''
continue语句
作用：跳过当前循环中的剩余语句，然后继续下一次循环
注意：只能跳过当前/距离最近的循环
'''
# for i in range(10):
#     print(i)
#     if i == 3:
#         continue
#     print("***")
#     print("&&&")

a = 100
while 1:
    for i in range(10):
        print(i)
        if i == 3:
            # 跳过剩余语句
            continue
        print("***")
        print("&&&")
    print("嗨嗨嗨")


