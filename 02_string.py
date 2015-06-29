#! /usr/bin/env python3
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


# str和bytes是不同的
# bytes的每个字符都只占用一个字节. b'str'这种形式的bytes, 默认是ascii编码的, 如果
# str是中文, 超出了ascii的表示范围, python会报错.
# 可以使用encode来编码为指定的bytes

# this line is an error example
# x = b'中文'

cn_bytes = '中文'.encode("utf-8")
print("'中文' encoding utf-8 is", cn_bytes)
print("%s decoding utf-8 is" % cn_bytes, cn_bytes.decode("utf-8"))

# 可以用ord和chr两个函数来对 字符--字符的整数表示 进行转换
ord_A = ord('A')
print("chr(%d) is" % ord_A, chr(ord_A))

ord_cn = ord('中')
print("chr(%d) is" % ord_cn, chr(ord_cn))

# len作用于str和bytes上, 效果是不同的
# - 作用于str, 计算的是str的字符数
# - 作用于bytes, 计算的是bytes的字节数
print("len(b'ABC') is", len(b'ABC'))
print("len('中文') is", len('中文'))
print("len('中文'.encode('utf-8')) is", len('中文'.encode('utf-8')))

