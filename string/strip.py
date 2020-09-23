'''
strip

Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）。
strip()方法语法：
	str.strip([chars]);
chars -- 移除字符串头尾指定的字符。

'''
a = '88888888test888'
ret = a.strip('8')
print(ret)