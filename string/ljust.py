'''
ljust

Python ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。
如果指定的长度小于原字符串的长度则返回原字符串。
ljust()方法语法：
	str.ljust(width[, fillchar])

width -- 指定字符串长度。
fillchar -- 填充字符，默认为空格。

'''

mystr = 'hello'
ret = mystr.ljust(10,'*')
print(ret)