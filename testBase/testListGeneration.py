#测试列表生成式

print([x*x for x in range(1,11)])

#有条件的列表生成式
print([x*x for x in range(1,11) if x%2==0])

#两次循环
print([m+n for m in 'ABD' for n in 'XYZ'])

d = {'x': 'A', 'y': 'B', 'z': 'C' }
c = ['A',1,'B']
#迭代元组
for k,v in d.items():
    print(k, '=', v)
#迭代列表,并输出下标
for i,v in enumerate(c):
    print(i, v)

#生成列表
print([k + '=' + v  for k,v in d.items()])

# 把列表中所有字母变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])
print("************分割线**************")

# 练习
# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
# -*- coding: utf-8 -*-
# 这是一个坑,不能在循环时删除列表元素
# 可以把符合条件的元素生成到新列表,或使用列表生成式,或者逆序遍历
# 这里用逆序遍历
def lowerStr(L):
    for i in range(len(L)-1, -1, -1):
        value = L[i]
        if(isinstance(value, str)):
            L[i] = value.lower()
        else:
            L.pop(i)
    return L
# 把符合条件的元素生成到新列表,其实用列表生成式完全可以替代
def lowerStr2(L):
    L2 = []
    for v in L:
        if isinstance(v, str):
            L2.append(v.lower())
    return L2

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]  #lowerStr(L1)

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')


