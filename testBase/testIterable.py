from collections import Iterable
from collections import Iterator
#集合和字符串都是可迭代对象
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance(100, Iterable))

# 而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，
# 直到最后抛出StopIteration错误表示无法继续返回下一个值了。
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。

print("************分割线*************")
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance((x for x in range(10)), Iterator))
print(isinstance('abc', Iterator))