'''
 删除元素

类比现实生活中，如果某位同学调班了，那么就应该把这个条走后的学生的姓名删除掉；在开发中经常会用到删除这种功能。
列表元素的常用删除方法有：

del：根据下标进行删除, 也可以删除掉整个列表对象,提前释放内存
pop：删除最后一个元素, 也可以删除单个指定元素 把删除的元素返回回来
remove：根据元素的值进行删除 如果要删除的元素值不再列表,会崩溃
clear: 清空这个列表 把列表中的元素删除干净,但是列表还在
'''

# 删除元素 del, pop, remove



# del 删除指定的元素(通过下标索引)
# 格式: del 列表名[下标索引]
# del 这个函数 是python内置函数
my_list = ["小明", 20, "小红", 32]
del my_list[1]
print(my_list)

# del 第二种用法 ----> 了解
# 提前杀死对象 提前释放内存
my_list1 = ["小明", 20, "小红", 32]
del my_list1

# pop是属于列表的方法
# pop 默认情况下 会从列表的后面开始删除
# .pop() 会有一个返回值 告知删除元素的值
my_list2 = ["小明", 20, "小红", 32]
print(my_list2.pop())
print(my_list2)

# pop(下标索引)
my_list3 = ["小明", 20, "小红", 32]
ret1 = my_list3.pop(0)
print(ret1)
print(my_list3)

# remove通过对象(数值)来删除列表中的元素
my_list4 = ["小明", 20, "小红", 32]
my_list4.remove('小红')
print(my_list4)

# clear 清空列表(列表中的所有元素全部删除)
my_list5 = ["小明", 20, "小红", 32]
my_list5.clear()
print(my_list5)

# clear() 等价于:  my_list = [] 或者 my_list = list()