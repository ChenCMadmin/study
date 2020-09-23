'''
 rfind

Python rfind() 返回字符串最后一次出现的位置(从右向左查询)，如果没有匹配项则返回-1。
rfind()方法语法：
	str.rfind(str, beg=0 end=len(string))
str -- 查找的字符串
beg -- 开始查找的位置，默认为 0
end -- 结束查找位置，默认为字符串的长度。

'''
mystr = 'hello world test and test2'
ret = mystr.rfind("test")
print(ret)