#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

# empty func
def nop():
    pass

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# a = my_abs('af')

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

a = move(1, 1, 80, math.pi / 6)
# a is a tuple!
print('a: ', a)

# 默认参数必须指向不变对象!!!
def add_end(L=[]):
    L.append('END')
    return L

print(add_end())
print(add_end())
print(add_end())

def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end2())
print(add_end2())
print(add_end2())

# 可变参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum

a = calc([1, 2, 3])
b = calc((1, 3, 5, 7))

def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum

# 自动把参数组装成 tuple
a = calc2(1, 2)
b = calc2()

c = [1, 2, 3]
a = calc2(*c)

# 关键字参数，自动组装成 dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('AAA', 30)
person('BBB', 35, city='Beijing', job='Engineer')

extra = {'city' : 'Beijing', 'job' : 'Engineer'}
person('BBB', 35, **extra)

# 命名关键字参数
def person2(name, age, *, city, job):
    print(name, age, city, job)

person2('Jack', 24, city='Beijing', job='Engineer')
# person2('Jack', 24, 'Beijing', 'Engineer')

def person3(name, age, *args, city, job):
    print(name, age, args, city, job)

# 参数组合
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)