# 定义一个列表
# 格式: 列表名 = [元素1, 元素2, 元素3,....]

my_list1 = ["xiaoming", "xiaohong"]
# # -> 支持下标索引
#
my_name = my_list1[0]
print(my_name)

# 定义一个列表
my_list2 = [10, 3.14, "hello", True]
print(my_list2)
# 需求 我想打印hello (从左到右) 0, 1, 2,....
# 也可以从右到左 -1, -2, -3, ....
ret1 = my_list2[-1]
print(ret1)


# 定义一个空列表
# my_list = []  或者 list()
# my_list = list()
# # 打印下元素个数
l = len(my_list2)
print(l)


'''
查找元素一般使用 in 或者 not in 或者 index count结合
in 或者 not in 我们搭配 if 语句来实现
如果单独使用 index 有崩溃的风险(index没有查找到元素的情况下,会崩溃)
要想使用index, 需要先判断元素在列表中的count值, 只有元素的个数大于等于1个, 代表列表中有此元素, 才可以用index进行下标值的获取, 这样比较安全, 排除了崩溃的可能.
我们这里不可以使用find 或者 rfind , 因为 find 和 rfind 是字符串常用的方法,我们这里说的是列表.
'''