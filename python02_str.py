#-- coding: utf-8 --

import string

# 去除空格
s= '    abc  qdsd  '
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s)

# 连接字符串
a = 'abc'
b = 'cba'
print(a + "\n" + b)

# 大小写
print(s.upper())
print(s.upper().lower())
print(s.capitalize())

# 位置比较
s1 = 'abcdefg'
s2 = 'ascasfg'
print(s1.index('abc'))
try:
	print(s2.index('abc'))
except ValueError:
	print('xxxx')

# 在python3里面。cmp函数被移除
print(s1==s2)
print(s1<s2)
print(s1>s2)
print('')

# 长度
print(len(s1))

try:
	print(len(None))
except :
	print('None,000')
print(len(''))
ss = ''
if ss is None:
	print('None')
if not ss:
	print('Empty')


# 分割和连接
slist = 'abc,efg,hij'
slist1 = slist.split(',')
print(type(slist1))
print (slist1)

srow = '''abc
asd
asd12
qwe'''
srow1 = srow.split('\n')
srow2 = srow.splitlines()
print(srow1)
print(srow2)
print('')

sa = ['asd','bbbb','aaa']
print(''.join(sa))
print('-'.join(sa))
print('\n'.join(sa))

# 常用判断
sb = 'fghadsas'
print(sb.startswith('fgh'))

print(sb.endswith('sas'))
print('1234abcd'.isalnum())
print('\t1234ab'.isalnum())
print('bacd'.isalpha())
print('1234'.isdigit())
print('       '.isspace())
print('abcsds123'.islower())
print('ABCD1234'.isupper())
print('Hello World'.istitle())

# 数字到字符串
print(str(5))
print(str(5.))
print(str(5.1235))
print(str(-123.123))

# 字符串到数字
print(int('1234'))
print(float('123.45'))
print(int(123.4522))







