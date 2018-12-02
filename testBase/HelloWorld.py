# def hello(name):
#     # str = 'Hello '+ name #返回一个字符串
#     str = 'Hello' , name  #返回一个元组
#     return str
#
# stk = hello('myName')
# print(stk)

# 命名关键字参数
# def person(name, age, **kw):
#     if 'city' in kw:
#         pass;
#     if 'job' in kw:
#         pass;
#     print("name:", name, "age:", age, "other:", kw)
# person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

# 命名关键字参数
# def person(name, age, *, city, job):
#     return print(name, age, city, job)
# def person2(name, age, *args, city, job):
#     print(name, age, args, city, job)
# print(person('gwf', 25, city='fdf', job='maNong'))
# print(person2('gwf', 25, 'fdfdsf', 'sdfsd34', city='fdf', job='maNong'))

#测试迭代
k = [(1, 1), (2, 4), (3, 9)]
for x, y in k:
    print(x, y)

# 1 1
# 2 4
# 3 9

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)