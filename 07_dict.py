#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

# 相当于其他语言中的map, 使用key-value方式存储
# 一个key只能对应一个value
# dict内部存放key的顺序，与key放入的顺序是没关系的

# 注意: dict的key， 必须是不可变对象, 此条适用于set
# 在python中, 字符串和整数是不可变的, 可以用作key; list是可变的, 就不能用作key
# 不可变对象, 调用对象自身的任意方法, 都不会改变该对象自身的内容. 这些方法会创建新
# 的对象并返回, 这样就保证了不可变对象自身永远是不可变的


# dict与list比较
# dict:
# 1. 查找和插入的速度极快， 不会随着key的增加而增加
# 2. 需要占用大量的内存， 内存浪费极多
# list:
# 1. 查找和插入的时间随着元素的增加而增加
# 2. 占用空间小， 浪费内存很少

# 定义一个dict
d = {'carl':29, 'tom':30, 'lucy':24}
print(d['carl'])

# 访问一个不存在的key， 会报错
# print(d['nobody'])
# Traceback (most recent call last):
      # File "./07_dict.py", line 17, in <module>
          # print(d['nobody'])
          # KeyError: 'nobody'

# 使用in来判断key是否存在于某个dict中
is_in = 'nobody' in d
print('"nobody" is in dict d?', is_in)
is_in = 'carl' in d
print("'carl' is in dict d?", is_in)

# 使用get方法来访问， key不存在时不会报错， 会返回none
print("get 'nobody' from d:", d.get('nobody'))

# 更新key的值
d['carl'] = 39
print('now "carl" is:', d['carl'])

# 遍历dict的几种方法
for i in d:
    print('dict[%s] =' % i, d[i])

for (k, v) in d.items():
    print('dict[%s] =' % k, v)

for k, v in zip(d.keys(), d.values()):
    print('dict[%s] =' % k, v)

# 遍历dict中的值
for v in d.values():
    print('v:', v)

# this is only supported in python2
# removed in python3
# for k,v in d.iteritems():
    # print('dict[%s] =' % k, v)

# 删除key
pop_element = d.pop('carl')
print(pop_element)

print("after pop out", pop_element, ', now d is:')
for (k, v) in d.items():
    print('dict[%s] =' % k, v)



# 判断一个对象是否可迭代
from collections import Iterable

print("\n判断一个对象是否可迭代")
print("is str  iterable?", isinstance('abs', Iterable))
print("is list iterable?", isinstance([1, 2, 3], Iterable))
print("is int  iterable?", isinstance(123, Iterable))

