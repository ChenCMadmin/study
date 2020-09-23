# 拆包: 对于函数中的多个返回数据, 去掉元组, 列表 或者字典 直接获取里面数据的过程.
print('=========1============')
# 对列表进行拆包
my_list = [1, 3.14, "hello", True]
num, pi, my_str, my_bool = my_list
# 或者
num, pi, my_str, my_bool = [1, 3.14, "hello", True]

print('==========2===========')
# 对元组进行拆包
my_tuple = (1, 3.14, "hello", True)
num, pi, my_str, my_bool = my_tuple

print('==========3===========')
# 对字典进行拆包
my_dict = {"name":"老王", "age": 19}
ret1, ret2 = my_dict
# 得到的是key  字典是无序的
print(ret1, ret2)

print('==========4===========')
# 用拆包的形式定义变量
# 一次定义多个变量
num1 = 10
num2 = 20
num3 = 30
num4 = 3.14
# # 龟叔 称之为比较pythonic 自夸
# # 变量名和值是一一对应
num1, num2, num3, num4 = 10, 20, 30, 3.14

print('==========5===========')
# 函数返回元组时直接拆包
# 对元组拆包:
def get_my_info():
    high = 178
    weight = 100
    age = 18
    return high, weight, age

# 这一步叫做拆包:
my_high, my_weight, my_age = get_my_info()
print(my_high)
print(my_weight)
print(my_age)