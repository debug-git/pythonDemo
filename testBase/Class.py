#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from types import MethodType
class Student(object):
    pass

s = Student()
s.name = 'myName'
print(s.name)

# 绑定一个方法
def set_age(self, age):
    self.age = age
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)
# 给一个实例绑定的方法，对另一个实例是不起作用的,以下会报错
# s2 = Student()
# s2.set_age(15)
# print(s2.age)

print('**********分割线*********')
# __slots__ 定义一个类只允许有的属性
# 使用@property, 可以设置只读属性
class Human(object):
    __slots__ = ('__age', '__name')

    def __str__(self):
        return ('Human Object (name: '+ self.__name+ '.age: '+ str(self.__age)+ ')')

    __repr__ = __str__

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise ValueError('年龄必须是整形数字!')
        if age<0 or age>150:
            raise ValueError('人类年龄必须在0-150之间!')
        self.__age = age


obama = Human()
obama.age = 151
obama.name = 'obama'
# obama.f = 'fdf'
print(obama)


# 多重继承遇到多个类的方法名相同会如何处理?
class RunableMixIn(object):
    def deal(self):
        print('I can run!')
class FlyableMixIn(object):
    def deal(self):
        print('I can fly!')
class Swan(FlyableMixIn, RunableMixIn):
    pass
    # def deal(self):
    #     print('能跑又能飞的天鹅就是本鹅了')

swan = Swan()
swan.deal()
# 当new一个子类时，调用多个父类中同名的方法，实际用的是第一个继承的类的方法！
# 如果覆盖了该方法，则调用的是子类的方法。