# 查找元素(in, not in, index, count)

# 定义一个列表, 判断老李是否在列表中
str = '老李'
my_list = ['老李', '老张', '小明', 300, 300]
if str in my_list:
    print('存在在列表中')
print('1============')


# 使用not in 判断一个元素不再列表中
if "小红" not in my_list:
    print("小红不再列表中")
print('not in============')

# index 通过index 获取某个元素在列表中的下表索引
ret1 = my_list.index(300)  #查询不到会报错
print(ret1)
print('index============')

# count查找某个元素的值在列表中出现的次数
ret2 = my_list.count(300)
print(ret2)
print('count============')

# 查询4000 如果有给出下标索引值 如果没有 什么也不做
# count配合index实现:
count = my_list.count(300)  #查询不到不会报错
if count > 0:
    index = my_list.index(300)
    print(index)
print('============')

# 使用in配合完成
if 300 in my_list:            #查询不到不会报错
    index = my_list.index(300)
    print(index)