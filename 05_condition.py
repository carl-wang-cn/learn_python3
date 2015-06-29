#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

age_str = input('please input your age:')

# input返回的是string类型的值, 需要把string转换成数字类型, 才能
# 用于下面的条件判断
age_int = int(age_str)
if age_int >= 18:
    print('your age is', age_int)
    print('adult')
elif age_int >= 6:
    print('your age is', age_int)
    print('teenager')
else:
    print('your age is', age_int)
    print('kid')


