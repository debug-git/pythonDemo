# -*- coding: utf-8 -*-
import time, functools
# 装饰器
f = lambda x : x ** 3

def quart (x):
    return x ** 2

print(quart.__class__)
print(quart.__code__)   #函数的绝对地址
print(quart.__name__)  #函数的名称

# 练习
# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
def metric(fn):
    def wrapper(fn):
        print('%s executed in %s ms' % (fn.__name__, 10.24))
        f
    return fn
# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')