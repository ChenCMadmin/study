'''
Python3 中有六个标准的数据类型：
Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）

Python3 的六个标准数据类型中：
不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

'''

num = 666
print("类型：%s"%type(num))

str = 'String'
print("类型：%s"%type(str))

list = [1, 2, 3]
print("类型：%s"%type(list))

tuple = (1, 2, 3)
print("类型：%s"%type(tuple))

#创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
set = {1, 2, 3}
print("类型：%s"%type(set))

#字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
dict = {'key':1, 'neme': 2, 'num':3}
print("类型：%s"%type(dict))





