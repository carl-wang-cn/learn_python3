#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Author: carl
# Created on: 2015-10-04
# History:

# 返回一个函数
# 闭包
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

# 当调用lazy_sum()时, 返回的并不是求和结果, 而是求和函数
f = lazy_sum(1, 3, 5, 7, 9)
print("f: ", f)
print("f(): ", f()) # 调用函数f()时, 才真正计算求和的结果

# 闭包
# 在函数lazy_sum中又定义了函数sum, 并且, 内部函数sum可以引用外部函数lazy_sum的参数
# 和局部变量, 当lazy_sum返回函数sum时, 相关参数和变量都保存在返回的函数中, 这种程序
# 结构被称为"闭包"

# 注意: 每次调用lazy_sum时, 都会返回一个新的函数, 即使传入相同的参数
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print("f1==f2?", f1==f2)

# 注意: 返回函数不要引用任何循环变量, 或者后续会发生变化的变量



# 匿名函数
# 使用lambda实现
# 注意: ":"前表示函数参数, ":"后, 只能有一个表达式, 不用写return, 返回值就是该表达式的结果
f = lambda x, y: x + y
print("f(3, 4) =", f(3, 4))




# 装饰器 decorator

import functools

# 1. 先定义一个decorator, 该decorator本身不需任何参数
def log(func):
    @functools.wraps(func)  # 如果没有这行, func.__name__就不在是原来的, 会变成wrapper
    def wrapper(*args, **kw):
        print("call %s()." % func.__name__)
        return func(*args, **kw)
    return wrapper

# 2. 再定义一个普通函数now

@log   # 3. 将decorator放到now的定义处, 此时, 调用now, 相当于调用log(now)
def now():
    print("now")

now()

# 4. 定义一个新的decorator, 该decorator本身需要参数
def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s %s():" % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# 5. 重新定义一个now2函数
@log2("execute")   # 同上
def now2():
    print("now2")

now2()
print("now's name:", now.__name__)
print("now2's name:", now2.__name__)




# 偏函数
# 定义: 使用functools.partial来定义, 作用就是, 把一个函数的某些参数给固定住(也就是设置默认值),
#       返回一个新的函数, 调用这个函数会更简单
int2 = functools.partial(int, base=8)
print("int('10001'):", int('10001'))
print("int('10001', base=8):", int('10001', base=8))
print("int2('10001'):", int2('10001'))
