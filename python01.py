# -- conding: utf-8 --

# print 基本数据类型的type
print(type(123))
print(type(112.32))
print(type(123.))
print(type('asdada'))
print('')

print(type([1,2,3,'w','b']))
print(type((1,'abc')))
print(type(set(['d','a',2])))
print(type({'a':1,'a':2}))
print('')

def func(a,b,c):
	print (a,b,c)

print(type(func))

a=func
print(type(a))

import string
print (type(string))

class MyClass(object):
	pass

print(type(MyClass))

my_class = MyClass()
print (type(my_class))








