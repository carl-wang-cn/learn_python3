#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

# python 有两种形式的loop
# 1. for ... in 形式
# 2. while 形式


# for ... in 形式
names = ["carl", "tom", "jerry"]
print(names, "遍历结果如下:")
for name in names:
    print(name)

sum = 0
for x in range(0, 101):
    sum = sum + x
print("for ... in 形式 计算0-100的和, 结果为:", sum)

# while 形式
sum = 0
n = 0
while n <= 100:
    sum = sum + n
    n = n + 1
print("while 形式 计算0-100的和, 结果为:", sum)



# 在07_dict.py中有几种遍历一个dict的方法
