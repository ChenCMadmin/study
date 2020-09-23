'''
所谓的列表推导式，就是指的轻量级循环创建列表
格式:
列表推导式的常见形式:
	my_list = [ item    for item in iterable]
	my_list: 列表名 (变量名,  属于标识符)
	item: 将要存放到列表中的内容
	for item in iterable:  非常标准的for循环表达式

	[expr for iter in iterable if cond_expr]
	expr: 将要存放到列表中的内容
	iter: 遍历的每一项内容
    iterable: 遍历的对象
    if cond_expr: 条件表达式, 只有满足当前条件的,才能存放到列表中.
'''

my_list = [x*x for x in range(10)]
print(my_list)

list = [x for x in range(3, 19, 2)]
print(list)

list = [x for x in range(3, 10) if x % 2 == 0]
print(list)

list = [11, 10, 9, 8, 7, 6]
[x for x in list if x % 2]

llist = [x for x in 'hello python' if x != ' ' and x != 'l']
print(llist)



