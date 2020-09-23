'''
rjust

Python rjust() 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串。
rjust()方法语法：
	str.rjust(width[, fillchar])
width -- 指定填充指定字符后中字符串的总长度.
fillchar -- 填充的字符，默认为空格

'''
mystr = "hello"
ret = mystr.rjust(10, '_')
print(ret)