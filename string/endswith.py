'''
Python endswith() 方法用于判断字符串是否以指定后缀结尾，
如果以指定后缀结尾返回True，否则返回False。可选参数"start"与"end"为检索字符串的开始与结束位置。
endswith()方法语法：
	str.endswith(suffix[, start[, end]])
suffix -- 该参数可以是一个字符串或者是一个元素。

start -- 字符串中的开始位置。

end -- 字符中结束位置。

'''
mystr = 'hello world itcast and itcastcpp'
x = mystr.endswith('cpp')
print(x)
y = mystr.endswith('app')
print(y)