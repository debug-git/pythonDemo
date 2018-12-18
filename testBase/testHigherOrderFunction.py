#高阶函数
# 把函数作为参数传入，这样的函数称为高阶函数，
# 函数式编程就是指这种高度抽象的编程范式。
# -*- coding: utf-8 -*-
from collections import Iterator, Iterable
from functools import reduce

# x = abs(-10)
x = abs;
print(x(-151))

def add(x, y, f):
    return f(x) + f(y)
print(add(-10, 12, abs))

print("*********分割线************")
# Python内建了map()和reduce()函数。下面来测试一下
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x*x;
r = map(f, range(10))
print(isinstance(r, Iterator))      #True
print(list(r))

print("*********分割线************")
# reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
def add(x, y):
    return x + y;
print(reduce(add, [1, 2, 3, 4, 5]))

print("*********字符串转数字分割线************")
# 如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，
# 我们就可以写出把str转换为int的函数：
# def fn(x, y):
#     return x * 10 + y
# def char2num(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return digits[s]
# # map(char2num, '13579')将该字符串转为数字的列表
# num = reduce(fn, map(char2num, '13579'))
# print(num)
# num2 = reduce(fn, list(map(char2num, '13579')))
# print(num2)

print("*********单个函数分割线************")
# 整理成一个函数
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# def str2int(str):
#     def char2num(s):
#         return DIGITS[s]
#     def fn(x, y):
#         return x * 10 + y
#     return reduce(fn, map(char2num, str))
# print(str2int("1011212"))

print('*********lambda函数分割线*********')
# 还可以用lambda函数进一步简化成：
def char2num(s):
    return DIGITS[s]
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
print(str2int("1011212"))


print('*********lambda函数分割线*********')
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    idx = s.find(".")
    prefix = s[ : idx]
    suffix = s[idx+1 : ]
    return str2int(prefix) + str2int(suffix)/(10**len(suffix))
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')