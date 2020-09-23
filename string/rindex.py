'''
 rindex

Python rindex() 返回子字符串 str 在字符串中最后出现的位置，
如果没有匹配的字符串会报异常，你可以指定可选参数[beg:end]设置查找的区间。
rindex()方法语法：
	str.rindex(str, beg=0 end=len(string))
str -- 查找的字符串
beg -- 开始查找的位置，默认为0
end -- 结束查找位置，默认为字符串的长度。

'''
mystr = 'hello world test and test2'
ret1 = mystr.rindex('test')
print(ret1)
print('============')
ret2 = mystr.rindex("IT")
print(ret2)