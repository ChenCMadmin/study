'''
center

Python center() 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。默认填充字符为空格。
center()方法语法：
	str.center(width[, fillchar])
width -- 字符串的总宽度。
fillchar -- 填充字符。

'''
mystr = 'hello world itcast and itcastcpp'
ret = mystr.center(50,'@')
print(ret)