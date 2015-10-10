#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Author: carl
# Created on: 2015-10-04
# History:


# 使用模块的好处
# 1. 提高代码的可维护性
# 2. 编写代码不必从零开始, 当一个模块编写完毕, 可以被其他地方引用
# 3. 避免函数名和变量名冲突

# 使用包的注意事项
# 1. 按目录来组织模块, 在目录中增加一个__init__.py的文件, 否则会被当成普通目录
# 2. 可使用多级子目录

# 作用域
# 1. __xxx__, 特殊变量, 通常有特殊用途
# 2. __xxx, _xxx, private变量, 不应该被直接引用, 但是python从语法上不强制


# 别名
try:
    import CstringIO as StringIO
except ImportError: # 导入失败会捕获到ImportError
    import StringIO

# python搜索第三方模块的路径
# 1. 默认情况下, python的搜索路径放在sys.path中
# 2. 添加我们自己的搜索目录, 可以`sys.path.append('/path/to/my/module')`, 运行时修改, 结束后失效

