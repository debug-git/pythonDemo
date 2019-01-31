#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 定义一个类,括号里是继承
class Student(object):
    def __init__(self, name, score):
        self.__name = name  #设置双下划线即为私有变量,不可直接访问.但可以通过"_类名__变量名"的方式非法访问,不推荐此做法
        self.score = score
    def print(self):
        print('%s: %s' % (self.__name, self.score))

bart = Student('bart', 80)
bart.print()
bart.age = 8  # 不同于Java,可以给实例随便添加属性
print(bart._Student__name)

#下面这句是会报错的,因为定义了构造函数之后必须传入参数
# sun = Student()
# sun.ff = "fdf"
# print(sun.ff)
print("**************下面在测试继承**************")

# 测试继承
class Animal(object):
    def run(self):
        print("动物在跑...")

class dog(Animal):
    def run(self):
        print("狗在跑...")
    def sleep(self):
        print("狗在睡觉...")

class cat(Animal):
    def run(self):
        print("猫在跑...")
    def sleep(self):
        print("猫在睡觉...")

a = Animal()
a.run()
a = dog()
a.run()
a.sleep()
b = cat()
b.run()
b.sleep()
print(isinstance(a, Animal))

print("***********测试多态*********")
def showAnimal(animal):
    print(animal.run())

showAnimal(a)
showAnimal(b)

print("*******************")
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
print(hasattr(obj, 'x'))  #是否有属性x ,返回True
print(hasattr(obj, 'y'))  #是否有属性y ,返回False
print(getattr(obj, 'x'))  #获取属性x的值
print(getattr(obj, 'fds')) #如果试图获取不存在的属性，会抛出AttributeError的错误,当报错时下面代码不会执行
print(getattr(obj, 'z', 'default')) #可以传入一个default参数，如果属性不存在，就返回默认值：
setattr(obj, 'name', 'newName') #setattr可以设置值
print(getattr(obj, 'name'))

print("*********练习**********")
# 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
class Student(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')