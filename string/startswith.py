'''
Python startswith() 方法用于检查字符串是否是以指定字符串开头，
如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，则在指定范围内检查。
startswith()方法语法：
	str.startswith(str, beg=0,end=len(string));
str -- 检测的字符串。

strbeg -- 可选参数用于设置字符串检测的起始位置。

strend -- 可选参数用于设置字符串检测的结束位置。


'''

mystr = 'hello world itcast and itcastcpp'
x = mystr.startswith("hello")
print(x)
y = mystr.startswith("Hello")
print(y)