#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# dict
d = {'AAA' : 95, 'BBB' : 65, 'CCC' : 87}
print('d[BBB]: ', d['BBB'])
print('Is \'CCC\' in d: ', 'CCC' in d)
print('d[DDD]: ', d.get('DDD'))
print('d[DDD]: ', d.get('DDD', -1))

d.pop('BBB')

# set
s = set([1, 2, 3, 3, 3, 2])
print('s: ', s)

s.add(5)
s.remove(3)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print('s1 & s2: ', s1 & s2)
print('s1 | s2: ', s1 | s2)