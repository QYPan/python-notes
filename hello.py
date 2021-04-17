print('hello, world')
print('aaa', 'bbb', 'ccc')
print(300)
print(100 + 200)
print('100 + 200 = ', 100 + 200)

name = input()
print('hello, ', name)

name = input('name: ')
print('hello, ', name)

# format
print('Hello, %s' % 'world')
print('Age: %s, Gender: %s' % (25, True))
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

print('2^4: ', 2 ** 4)

r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')