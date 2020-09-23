'''
Python find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。
find()方法语法：
	str.find(str, beg=0, end=len(string))
sub: 要查找的小字符串
start: beg -- 开始索引，默认为0。
end: end -- 结束索引，默认为字符串的长度。

'''

mystr = "hello world itcast and itcastcpp"
ret1 = mystr.find("itcast")
print(ret1)