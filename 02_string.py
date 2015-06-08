#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 在string前用r修饰, 表示string的内容无需转义
# '''string''' 可以使用多行表示字符串

r_str = r"I'm sure that \ here is not transferred! \\\\\\"
multi_line_str = '''the 1st line
the 2nd line
the 3rd line
the 4th line
'''

print(r_str)
print(multi_line_str)
