# 测试排序
L = sorted([36, 5, -12, 9, -21], key=abs)
L2 = sorted([36, 5, -12, 9, -21])
print(L)
print(L2)

print('***********************')
#对字符串，默认按照ASCII码排序
strList = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(strList) # 输出结果['Credit', 'Zoo', 'about', 'bob']

#自定义排序规则，将所有字符转小写在排序
strList2 = sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower)
print(strList2) # 结果：['about', 'bob', 'Credit', 'Zoo']

#反序排列
strList3 = sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower, reverse = True)
print(strList3) # 结果 ['Zoo', 'Credit', 'bob', 'about']