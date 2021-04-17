#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO
from io import BytesIO

try:
    f = open('file.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

with open('file.txt', 'r', encoding='gbk', errors='ignore') as f:
    for line in f.readlines(): # readlines() return a list
        print(line.strip()) # 把末尾的 '\n' 删掉

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())