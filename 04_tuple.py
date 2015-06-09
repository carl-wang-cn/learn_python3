#! /usr/bin/env python
# -*- encoding: utf-8 -*-


# tuple, 也是有序集合, 跟list比, 一旦定义就不能再改变
# tuple不支持insert, update, append, pop这些操作
# tuple因为不能改变, 代码更安全, 尽量用tuple代替list


# 定义空tuple
empty_t = ()
print(empty_t)

# 定义只有一个元素的tuple, 注意那个逗号
single_t = (1,)
print(single_t)

