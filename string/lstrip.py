'''
 lstrip

Python lstrip() 方法用于截掉字符串左边的空格或指定字符。
lstrip()方法语法：
	str.lstrip([chars])
chars --指定截取的字符。

'''
str = "     this is string example....wow!!!     ";
print(str.lstrip())
str = "88888888this is string example....wow!!!8888888";
print(str.lstrip('8'))