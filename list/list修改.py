# 定义一个列表
my_list = ['ab',23, 2.23]

# 获取
value = my_list[1]
print(value)

# 把获取的数据进行修改
my_list[1] = "22222"
print(my_list)


my_list[-1] = 223
print(my_list)

'''
修改元素只需要遵循如下顺序: 先获取, 后修改
在列表中获取元素只需要根据下标索引值拿取.
修改时, 那刚刚拿取的元素重新赋值即可.
列表是可变的, 所以里面的元素也是可以修改的.
'''