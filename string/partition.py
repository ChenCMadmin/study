'''
partition

partition() 方法用来根据指定的分隔符将字符串进行分割。

如果字符串包含指定的分隔符，则返回一个3元的元组，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串。

partition() 方法是在2.5版中新增的。
partition()方法语法：
	str.partition(str)
str : 指定的分隔符。

'''

mystr = 'hello world test and test2'
ret = mystr.partition('test')
print(ret)