'''
 rpartition

类似于 partition()函数,不过是从右边开始.
rpartition()方法语法：
	str.partition(str)
str : 指定的分隔符。

'''

mystr = 'hello world test and test2'
ret1 = mystr.partition('test')
print(ret1)
ret2 = mystr.rpartition('test')
print(ret2)