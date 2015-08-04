#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

# 类似c++中的set, 存储一组不重复的key
# 无序
# 同dict一样, set中的key必须为不可变对象


# 定义一个set, 需要提供一个list作为输入集合
s = set([1, 2, 3])
print(s)

# 重复的元素会被自动过滤
s = set([1, 1, 2, 3, 4, 4])
print(s)

# 向set中添加元素
print('add 5 in')
s.add(5)
print(s)
print('add 5 again')
s.add(5) # 重复添加, 没啥用
print(s)

# 删除元素
s.remove(4)
print('remove 4')
print(s)

s1 = ({1, 2, 3})
s2 = ({2, 3, 4, 5})
print("s1:", s1)
print("s2:", s2)
print("s1&s2", s1 & s2)
print("s1|s2", s1 | s2)

