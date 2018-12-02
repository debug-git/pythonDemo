# 练习
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
# 参考java的trim()方法,从开头和结尾分别找空格,然后去除
# -*- coding: utf-8 -*-
def trim(s):
    end = len(s)
    begin = 0
    while begin < end and s[begin] <= ' ':
        begin = begin + 1
    while begin < end and s[end-1] <= ' ':
        end = end-1
    if begin > 0 or end < len(s):
        s = s[begin:end]
    return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')