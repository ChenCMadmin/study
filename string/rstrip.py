'''
rstrip

Python rstrip() 删除 string 字符串末尾的指定字符（默认为空格）.
rstrip()方法语法：
	str.rstrip([chars])
chars -- 指定删除的字符（默认为空格）

'''
mystr = '888888hello888888'
ret = mystr.rstrip('8')
print(ret)
