#!/usr/bin/python3
# -*- coding: utf-8 -*-

name = input('please enter your name:')
print('hello', name)

# 注意, input返回的值是string类型, 即使你输入的是一个数字, 在条件判断语句里尤其要注意这点
num = input('please enter a number:')
print(type(num))

# print可以打印多个参数, 参数用逗号','分隔, 遇到逗号',', python会
# 输出一个空格
