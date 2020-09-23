'''
函数的返回值
什么是返回值:
“返回值”: 就是程序中的函数执行完成后，返回回来的数据.
其中: 一个函数可以有返回值也可以没有返回值,这个要看业务需求
返回值可以是多种多样的, 任何类型都有可能
函数返回数据的时候用的关键字是 return
'''

# 1、定义一个带有返回值的函数
def func1():
    print('你好,这里是函数内部')
    return '函数调用完成'

# 2、定义一个带有返回值的函数
def func2(a, b):
    print('你好,这里是函数内部')
    return a + b

# 3、定义一个带有返回值的函数
def func3():
    print('你好,这里是函数内部')
    return True

print('===================')
# 接收函数返回值
# 函数调用后,如果有返回值, 我们可以定义一个变量来进行接收.
#定义函数
def add2num(a, b):
    return a+b

print('===================')
#调用函数，顺便保存函数的返回值
result = add2num(100, 98)
#因为result已经保存了add2num的返回值，所以接下来就可以使用了
print(result)

print('===================')
# 函数的递归调用
# def deep(num):
#     print(num)
#     if num == 20:
#         return
#     num += 1
#     return deep(num)
#
# deep(1)

print('===================')
# python 学习了 一个内置函数 len(object)
# 定一个字符串
my_str = "hello"
# 内置函数如何实现的
def my_len(object):
    num = 0
    # 猜测
    for i in object:
        num += 1
    # 如果有一个return 数值 成为这个函数有返回值
    return num

my_l = my_len(my_str)
# None 没有返回值 空值类型
print("自定义的:",my_l)

l = len(my_str)
print(l)

print('===================')

'''
函数可以有返回值,也可以没有
函数的返回值自定
程序读取到return 关键字后, 就会退出当前的函数体, 即 return之后的代码将不会执行
如果return 后面有内容, 则返回return后面的内容, 如果单独写一个return, 即 return后面没有写明返回内容,则返回None, 但是函数体的执行到此仍然结束, 不再往下执行.
有时候,我们会把 return 当成跳出当前函数的方式来使用, 而不是用它返回内容.
'''

print('===================')
# 一个函数中可以有多个return语句，但是只要有一个return语句被执行到，那么这个函数就会结束，因此后面的return是没什么用处的
# 但是下面这样的情况中, return都会被调用到:

def create_nums(num):
    if num > 100:
        return '大于100'
    else:
        return '小于100'
create_nums(98)

print('===================')
# 函数根据有没有参数，有没有返回值可以相互组合
# 定义函数时，是根据实际的功能需求来设计的，所以不同开发人员编写的函数类型各不相同
# 四种函数的类型
# 01- 无参数无返回值
# 02- 无参数有返回值
# 03- 有参数无返回值
# 04- 有参数有返回值

# 01- 无参数无返回值
def my_print():
    print("你好")
    print("python")

# 执行函数
my_print()

# 02- 无参数有返回值
def my_pi():
    return 3.1415926

print(my_pi())


# 03- 有参数无返回值
def print_info(name):
    print("你好%s" % name)

print_info("龟叔")

# 定义一个列表
name_list = ["龟叔", "小明", "小红", "张三"]

for new_name in name_list:
    # print(new_name)
    print_info(new_name)



# 04- 有参数有返回值
def my_func(a, b):
    ret = a - b
    return ret

def my_func(a, b):
    return a - b

result = my_func(10, 5)
print(result)