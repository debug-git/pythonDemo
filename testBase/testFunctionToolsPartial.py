#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 第1行和第2行是标准注释，第1行注释可以让这个文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码；
import functools
# 测试偏函数
# 在介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。

print(int('123'))

# 假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去：
def int2(x ,base=2):
    return int(x , base)
print(int2('-10000000', 2))

print("************偏函数**************")
# python已经提供了偏函数了
int3 = functools.partial(int, base=2)
print(int3("-10000000"))

max2 = functools.partial(max, 10)
print(max2(5, 4, 3))

# 在上面这个例子,实际上会把10作为*args的一部分自动加到左边，也就是：
# max2(5, 4, 3)
# 相当于
args = (10, 5, 6, 7)
print(max(*args))