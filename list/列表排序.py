# 导入模块
import random

'''
sort
对列表中的元素进行排序。
sort()方法语法：
	list.sort([func])
func -- 可选参数, 如果指定了该参数会使用该参数的方法进行排序。

reverse
倒排列表中的元素。
'''
# 定义一个列表  列表中有6个元素
# 六个元素的每个数值范围:  [-10, 50]
# python3.x中排序只支持数字类型
# 定义一个空的列表 用来保存数据
my_list = []
# for
for i in range(6):
    value = random.randint(-10,50)
    # 把随机数添加到列表中
    my_list.append(value)

print(my_list)

print('===================')
# 排序, 默认是升序排列
my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)
print('===================')
# 降序排列
my_list.sort(reverse=True)
print(my_list)

print('===================')
# 实现对一个元素全为数字的列表 求最大值, 最小值
# 准备一个列表
my_list = [-1,-2,-3,-63,-20,-203]

# 定义一个变量,记录最大值
print(max(my_list))
max = my_list[0]
for value in my_list:
    if value > max:
        max = value
print(max)

print('===================')
# 定义一个变量 记录最小值
print(min(my_list))
min = my_list[0]
for value in my_list:
    if value < min:
        min = value
print(min)