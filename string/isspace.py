'''
 isspace

Python isspace() 方法检测字符串是否只由空格组成。
isspace()方法语法：
	str.isspace()

'''

mystr = 'abc123'
ret = mystr.isspace()
print(ret)

mystr1 = ''
ret1 = mystr1.isspace()
print(ret1)

mystr2 = '  '
ret2 = mystr2.isspace()
print(ret2)

mystr3 = '    '
ret3 = mystr3.isspace()
print(ret3)