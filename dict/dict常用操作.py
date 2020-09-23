# 定义一个字典
my_dict = {"name": "小红", "age": 22, "no": "009"}

# <1>len()
# 测量字典中，键值对的个数
l = len(my_dict)
print("元素数:%d" % l)


# <2>keys
# 返回一个包含字典所有KEY的列表
keys = my_dict.keys()
print(keys)
# dict_keys(['name', 'age', 'no'])其实就是列表类型 dict_keys
# 如果想转成list类型也可以
print(list(keys))


# <3>values
# 返回一个包含字典所有value的列表
values = my_dict.values()
print(values)
print(list(values))


# <4>items -> 最外层是一个列表 每个元素是一个元组 (元素1(key), 元素2(value))
items = my_dict.items()
print(items)
# [('name', '小红'), ('age', 22), ('no', '009')]
my_list = list(items)
# 获取no ('no', '009')
# print(my_list[2][0])



