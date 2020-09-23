'''
isalnum

Python isalnum() 方法检测字符串是否由字母和数字组成。
isalnum()方法语法：
	str.isalnum()

'''

mystr1 = '123'
ret1 = mystr1.isalnum()
print(ret1)

mystr2 = 'abc'
ret2 = mystr2.isalnum()
print(ret2)

mystr3 = 'abc123'
ret3 = mystr3.isalnum()
print(ret3)

mystr4 = 'abc 123'
ret4 = mystr4.isalnum()
print(ret4)