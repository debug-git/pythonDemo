#测试迭代
k = [(1, 1), (2, 4), (3, 9)]
for x, y in k:
    print(x, y)
print('**********分割线***********')
# 1 1
# 2 4
# 3 9

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
print('**********分割线***********')

#     练习
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
# -*- coding: utf-8 -*-
def findMinAndMax(L):
    length = len(L)
    if length == 0:
        return (None, None)
    elif length == 1:
        return (L[0],L[0])
    elif length > 1:
        # 自己造轮子,选择排序
        # j=0
        # while j<length-1:
        #     k = j+1
        #     while k<length:
        #         if L[j]>L[k]:
        #             temp = L[j]
        #             L[j] = L[k]
        #             L[k] = temp
        #         k = k+1
        #     j = j+1
        #利用已有方法
        minValue = min(L)
        maxValue = max(L)
        # sorted() 这个方法可以用来排序
        return (minValue,maxValue)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
print('**********分割线***********')
def testDict(k):
    k['a']='a2'
def testString(s):
    s = 'hhhhhhhh'

#证明python对list和dict的参数传值是引用传递
k = [7, 1, 3, 9, 5]
findMinAndMax(k)
print(k)
d = {'a':'123','b':456}
testDict(d)
print(d)

#证明python对字符串的参数传值是值传递,
s = 'test'
testString(s)
print(s)
# 总结:Python参数传递采用的肯定是“传对象引用”的方式。如果函数收到的是一个可变对象（比如字典或者列表）的引用，
# 就能修改对象的原始值－－相当于通过“传引用”来传递对象。如果函数收到的是一个不可变对象（比如数字、字符或者元组）的引用，
# 就不能直接修改原始对象－－相当于通过“传值'来传递对象。

print(sorted([7, 1, 3, 9, 5]))