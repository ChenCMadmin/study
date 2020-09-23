'''
splitlines

Python splitlines() 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
splitlines()方法语法：
	str.splitlines([keepends])
keepends -- 在输出结果里是否去掉换行符('\r', '\r\n', \n')，默认为 False，不包含换行符，如果为 True，则保留换行符。

'''

mystr = 'hello\nworld'
print(mystr)
ret = mystr.splitlines()
print(ret)