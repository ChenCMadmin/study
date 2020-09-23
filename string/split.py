'''
split

Python split()通过指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个子字符串
split()方法语法：
	str.split(str="", num=string.count(str)).
str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。

num -- 分割次数。

'''
name = 'hello world ha ha'
x = name.split(" ")
print(x)
y = name.split(" ", 1)
print(y)