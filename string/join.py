'''
 join

Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
join()方法语法：
	str.join(sequence)
sequence -- 要连接的元素序列。

'''

str = ' '
li = ['my', 'name', 'is', 'meiZong']
ret = str.join(li)
print(ret)

str1 = '_'
ret1 = str1.join(li)
print(ret1)