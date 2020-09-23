'''
常用的数据类型转换

函数	说明
int(x )	       将x转换为一个整数
float(x )	   将x转换为一个浮点数
complex(x)     将x转换到一个复数，实数部分为 x，虚数部分为 0。
complex(x, y)  将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。
str(x )	       将对象 x 转换为字符串
repr(x )	   将对象 x 转换为表达式字符串
eval(str )	   用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s )	   将序列 s 转换为一个元组
list(s )	   将序列 s 转换为一个列表
chr(x )	       将一个整数转换为一个Unicode字符
ord(x )	       将一个字符转换为它的ASCII整数值
hex(x )	       将一个整数转换为一个十六进制字符串
oct(x )	       将一个整数转换为一个八进制字符串
bin(x )	       将一个整数转换为一个二进制字符串

'''

x = 100

print(int(x))