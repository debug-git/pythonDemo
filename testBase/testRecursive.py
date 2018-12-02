# 测试递归
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

print(fact(2000))


# def kkk():
#     for x in list(range(10)):
#         print(x)
# kkk()