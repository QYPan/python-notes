#!/usr/bin/env python3
# -*- coding: utf-8 -*-

names = ['AAA', 'BBB', 'CCC']
for name in names:
    print(name)

sum = 0
for x in range(5):
    sum += x
print('sum: ', sum)

sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print('sum: ', sum)