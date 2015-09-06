#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

# 列表生成式
# 使用列表生成式, 可以生成非常简洁的代码

print("列表生成式")
print("===================")
# 生成list
l = list(range(1, 11))
print("l:", l)


l2 = []
for x in range(1, 11):
    l2.append(x*x)
print("l2:", l2)

l2 = [x * x for x in range(1, 11)]
print("l2:", l2)
# 上面两种l2的生成方式, 简洁度是显而易见的吧


# 带条件的列表生成式
l3 = [x * x for x in range(1, 11) if x % 2 == 0]
print("l3:", l3)


# 双层循环生成全排列
l4 = [ m + n for m in 'ABC' for n in 'XYZ']
print("l4:", l4)


print("===================\n")
print("生成器")
print("===================")
# 生成器
# 将列表生成式的[]改为(), 就变成了一个生成器

g = (x * x for x in range(1, 11))
print("g:", g)
for x in g:
    print(x)

print("===================")
# 斐波那契数列生成器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n = n + 1
    return 'done'

print(fib(6)) # 这里可以看的有'done'输出
print("===================")

# 将上面的函数改成一个生成器, 只需改一行即可
def fib_generator(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    return 'done'

# 最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，
# 遇到return语句或者最后一行函数语句就返回。而变成generator的函
# 数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时
# 从上次返回的yield语句处继续执行。
for x in fib_generator(6):
    print(x) # 这里发现没有看到'done'输出

print("===================")
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在
# StopIteration的value中:
g = fib_generator(6)
while True:
    try:
        x = next(g)
        print(x)
    except StopIteration as e:
        print("generator returned value:", e.value)
        break

