'''
title

Python title() 方法返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写。
title()方法语法：
	str.title();

'''
a = "hello itcast and itcastCPP"
x = a.title()
print(x)

# (见 istitle()方法检测字符串中所有的单词拼写首字母是否为大写,且其他字母为小写)？
b = "Hello Itcast And Itcastcpp"
x = b.istitle()
print(x)