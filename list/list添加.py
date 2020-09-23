# 列表中添加元素的方法有三种:
# append
# extend
# insert

# append:
# 只要是python中的对象,都可以插入
my_list = ['12','23',23, 34]
my_list.append(2323)
print(my_list)
my_list.append(True)
print(my_list)
my_list.append("2323")
print(my_list)
my_list.append("12")
print(my_list)
my_list.append(3.134)
print(my_list)
my_list.append([23,'2323'])
print(my_list)

# extend:
# 添加一个可以遍历的对象
my_list.extend([3,2,4,5,2])
print(my_list)
my_list.extend('hahhaha')
print(my_list)
# my_list.extend(2323)   # extend添加的对象需要可以遍历,这样写是错误的
# print(my_list)
# my_list.extend(True)   # extend添加的对象需要可以遍历,这样写是错误的
# print(my_list)
my_list.extend("2323")
print(my_list)
my_list.extend("12")
print(my_list)
# my_list.extend(3.134)  # extend添加的对象需要可以遍历,这样写是错误的
# print(my_list)
my_list.extend([23,'2323'])
print(my_list)

# insert 插入到制定位置
my_list1 = []
my_list1.insert(0,'hello')
print(my_list1)

'''
append和extend给列表添加元素都是从列表的尾部添加, insert是在指定位置添加.
append 添加的元素不限制类型, 任意对象都可以使用append加入列表
extend加入列表的元素有限制: 只有能够遍历的对象才可以, 并且添加到列表的元素是对象遍历之后的每一小部分.
目前我们所学的能够遍历的对象只有: 字符串和列表 (后期还会有元组 和 字典)
列表加入元素的方式可以根据需求随意选择
'''