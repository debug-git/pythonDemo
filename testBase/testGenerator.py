# 测试生成器
g = (x*x for x in range(10))
for o in g:
    print(o)

print("*************分割线************")
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
o = odd()
next(o)
next(o)
next(o)

print("*************分割线************")
def fib(max):
    n, a, b = 0, 0, 1
    while n<max:
        yield b
        a, b = b, a+b
        n = n + 1
    return 'done'
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break