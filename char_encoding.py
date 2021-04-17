#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# in py3, string is unicode
print('包含中文的str')
print('ord(\'A\'): ', ord('A'))
print('ord(\'中\'): ', ord('中'))

print('chr(\'66\'): ', chr(66))
print('chr(\'25991\'): ', chr(25991))

print('\u4e2d\u6587')

# network transmission
x = b'ABC'

# local -> net
print('\'ABC\'.encode(\'ascii\'): ', 'ABC'.encode('ascii'))
print('\'中文\'.encode(\'utf-8\'): ', '中文'.encode('utf-8'))

# net -> local
print('b\'ABC\'.decode(\'ascii\'): ', b'ABC'.decode('ascii'))
print('b\'\\xe4\\xb8\\xad\\xe6\\x96\\x87\'.decode(\'utf-8\'): ', b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print('len(ABC): ', len('ABC'))
print('len(中文): ', len('中文'))

print('len(b\'ABC\'): ', len(b'ABC'))
print('len(b\'中文\'): ', len('中文'.encode('utf-8')))
