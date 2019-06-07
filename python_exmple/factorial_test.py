#!/usr/bin/python3
# File name : factorial

# 通过用户输入数字计算阶乘

# 获取用户输入的数字
num = int(input("Please input a number: "))
factorial = 1

# 查看数字是负数，0或者正数
if num < 0:
    print('负数没有阶乘!')
elif num == 0:
    print('0的阶乘是1')
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print('%d 的阶乘为%d' % (num, factorial))
