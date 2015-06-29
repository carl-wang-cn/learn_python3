#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

# list是有序类型
# list中的元素可以不同类型
# 访问list中的元素, 用index, index从0开始, -1表示最后一个元素
# 向list中添加元素, append(value)添加元素到list末尾,
#                   insert(index, value)向指定位置添加元素
# 删除list中的元素用pop(index), pop()删除最后一个元素
# 更新list中的元素, 直接使用index来赋值即可
# 获取list中元素个数, 使用len()函数


devices = ["monitor", "keyboard", "mouse"]

# access
print("devices[1] is", devices[1])
print("devices[-1] is", devices[-1])
print("devices have", len(devices), "elements now, they are:")
for element in devices:
    print("\t", element)

# add element
devices.append('disk')
print("after append 'disk' into devices, now devices have", len(devices), "elements, they are:")
for element in devices:
    print("\t", element)

devices.insert(2, 'cdrom')
print("after insert 'cdrom' to index=2 postion, now devices have", len(devices), "elements, they are:")
for element in devices:
    print("\t", element)

# delete element
device = devices.pop()
print("after pop(), now devices have", len(devices), "elements, they are:")
for element in devices:
    print("\t", element)

print("the element that was poped is", device)

device = devices.pop(1)
print("after pop(1), now devices have", len(devices), "elements, they are:")
for element in devices:
    print("\t", element)

print("the element that was poped is", device)

# update with different-type element
devices[2] = 123456
print("after devices[2] = 123456, now devices have", len(devices), "elements, they are:")
for element in devices:
    print("\t", element)

