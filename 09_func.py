#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

# 调用函数
# 调用函数时, 如果传入的参数数量不对或类型不对, 会报TypeError错误
# abs(1, 2)
# Traceback (most recent call last):
# File "./09_func.py", line 12, in <module>
# abs(1, 2)
# TypeError: abs() takes exactly one argument (2 given)

print('')
print("python函数调用>>>>>>>>>>")
print("abs(-1):", abs(-1))
# 函数名其实就是指向一个函数对象的引用, 完全可以把函数名赋给一个变量,
# 相当于给这个函数起了一个"别名"
a = abs
print("a = abs, a(-1):", a(-1))

# python的数据类型转换
print('')
print("python的类型转换>>>>>>>>>>")
print("int('123'):", int('123'))
print("int(12.34):", int(12.34))
print("float('12.34'):", float('12.34'))
print("str(1.23):", str(1.23))
print("str(100):", str(100))
print("bool(1):", bool(1))
print("bool(''):", bool(''))


# 定义函数
def my_abs(x):
    # 对参数进行类型检查
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        return -x
# 如果函数没有显式地return, 那么函数会 return None

# 多个返回值
def swap(a, b):
    tmp = a
    a = b
    b = tmp
    return a, b

print('')
print("python函数返回多个返回值>>>>>>>>>>")
a = 1
b = 2
print("a =", a, " b =", b)
a, b = swap(a, b)
print("a =", a, " b =", b)

# 多个返回值, 其实返回的是一个tuple
r = swap(a, b)
print(r)


# 参数
# python除了正常定义的必选参数外, 还可以使用默认参数, 可变参数和关键字参数
# 这3种参数的使用顺序, 必须是: 必选参数->默认参数->可变参数->关键字参数
## 默认参数, 必须放在必选参数的后面可变参数
### 默认参数, 一定要指向不可变对象
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print('')
print("默认参数>>>>>>>>>>")
print("power(2):", power(2))
print("power(2, 3):", power(2, 3))

## 可变参数
### 在参数前面增加一个*, 就是可变参数
### 下面函数的numbers, 在函数内部实际上接收到的是一个tuple, 但是可以传入0-任意个实参
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print('')
print("可变参数>>>>>>>>>>")
print("calc():", calc())
print("calc(1, 2, 3, 4): ", calc(1, 2, 3, 4))

### 如果已有一个list或者tuple, 可以如下调用变参函数
nums = [1, 2, 3]
print("nums[]:", nums)
print("calc(*nums):", calc(*nums))

## 关键字参数
### 可变参数在函数内部将传入的参数组装成一个tuple, 而关键字参数将接收到的含参数名的参数
### 在函数内部组装成一个dict.
def person(name, age, **kw):
    print("name:", name, "age:", age, "other:", kw)

print('')
print("关键字参数>>>>>>>>>>")
person('carl', 29)
person('carl', 29, gender='male', nation='China')

## 几种参数组合使用
def func(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

print('')
print("python几种参数混合使用, 要注意顺序>>>>>>>>>>")
print("func(1, 2)")
func(1, 2)
print("func(1, 2, c=3)")
func(1, 2, c=3)
print("func(1, 2, 3)")
func(1, 2, 3)
print("func(1, 2, 'a', 3, 'b')")
func(1, 2, 'a', 3, 'b')
print("func(1, 2, 3, 'a', 'b')")
func(1, 2, 3, 'a', 'b')
print("func(1, 2, 3, 'a', 'b', x=99)")
func(1, 2, 3, 'a', 'b', x=99)

args = (1, 2, 3, 4)
kw = {'x':99}
print('args:', args)
print('kw:', kw)
print("func(*args, **kw)")
func(*args, **kw) # 要注意此行的输出

## python的变参和关键字参数使用*args和**kw是习惯写法, 也可以使用其他的参数名, 但是建议使用
## 习惯用法

# 递归函数
## 递归函数可以做的都可以使用循环来完成
## 使用递归函数容易导致栈溢出, 不建议使用, 故此处也不写demo了




