#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# \d 一个数字
# \w 一个字母或数字
# . 任意字符
# + 至少一个字符
# ？ 0 或 1 个字符
# {n} n 个字符
# {n,m} n~m 个字符
# \s 可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格，例如匹配' '，' '等

# [0-9a-zA-Z\_] 可以匹配一个数字、字母或者下划线
# [0-9a-zA-Z\_]+ 可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等
# [a-zA-Z\_][0-9a-zA-Z\_]* 可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量
# [a-zA-Z\_][0-9a-zA-Z\_]{0, 19} 更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）

# A|B 可以匹配 A 或 B，所以 (P|p)ython 可以匹配 'Python' 或者 'python'
# ^ 表示行的开头，^\d 表示必须以数字开头
# $ 表示行的结束，\d$ 表示必须以数字结束

if re.match(r'^\d{3}\-\d{3,8}$', '010-12345'):
    print('ok')
else:
    print('failed')

print('a b   c'.split(' '))
print(re.split(r'\s+', 'a b   c'))
print(re.split(r'[\s\,]+', 'a,b,   c'))

# group '()'
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())

# 贪婪匹配
print(re.match(r'^(\d+)(0*)$', '102300').groups())
print(re.match(r'^(\d+?)(0*)$', '102300').groups())

# 预编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())