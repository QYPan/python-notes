#!/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates = ['AAA', 'BBB', 'CCC']
first1 = classmates[0]
first2 = classmates[-3]
print('first1: %s, first2: %s' % (first1, first2))

classmates.sort()

classmates.append('DDD')
print('classmates: ', classmates)

classmates.pop()
classmates.pop(1)
print('classmates: ', classmates)

L = ['A', 123, True, ['B', False]]
print('L: ', L)

# tuple (can not change element)
classmates = ('AAA', 'BBB', 'CCC')

t = (1,)