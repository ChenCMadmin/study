'''
元组, 英文为 tuple
Python的元组与列表类似，不同之处在于元组的元素不能修改。元组使用小括号，列表使用方括号。
元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
'''

 # 元组和列表相比: 列表是可变的, 元组是不可变的

 # 定义一个字符串 '' 或者 ""
 # 定义一个列表 []
 # 定义一个元组 ()

 # 定义一个元组
my_tuple = (1, 3.14, True, 'HELLO')
# 查看数据类型
print(type(my_tuple))

# 定义一个空元组
my_tuple = ()
print(type(my_tuple))
my_tuple1 = tuple()
print(type(my_tuple1))

# 特例:
# 如果元组中只有一个元素
# 如下写法是错误的:  <class 'int'>
my_tuple2 = (1)
print(type(my_tuple2))

# 如下写法才是正确的:  <class 'tuple'>
my_tuple3 = (1,)
print(type(my_tuple3))

# 元组也可以通过下标获取元组中的元素
my_tuple4 = (1, 3.14, True, 'Hello')
# 获取3.14
value = my_tuple4[1]
print(value)

# 是否可以通过下标来修改元组中的值:
# 因为元组是不可改变的 不可以修改元素 或者删除元素
# my_tuple4[2] = 'world'
# print(my_tuple4)


# index count
# 我们是否可以根据index和count获取某个元素的位置?
index = my_tuple4.index(3.14)
print(index)

# 获取某个元素的个数
count = my_tuple4.count(3.14)
print(count)

# for循环遍历:
for value in my_tuple4:
    print(value)

# while循环遍历:
index = 0
length = len(my_tuple4)
while index < length:
    value = my_tuple4[index]
    print(value)
    index += 1