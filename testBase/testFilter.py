#测试过滤器，对列表进行过滤，只留下符合条件的元素

def fn(s):
    return s % 2 == 0
L = list(range(20))
print(list(filter(fn, L)))
