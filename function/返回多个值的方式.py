# 返回多个值的方式：函数的return 后面, 直接返回一个元组, 列表 或者 字典等.
def function1():
    return [1, 2, 3]        #列表

def function2():
    return (1, 2, 3)        #元组

def function3():
    return {"num1": 1, "num2": 2, "num3": 3}        #字典

# 调用函数,获取里面的数据
ret1 = function1()
print(ret1[0])
print(ret1[1])
print(ret1[2])

# 调用函数,获取里面的数据
ret2 = function2()
print(ret2[0])
print(ret2[1])
print(ret2[2])

# 调用函数,获取里面的数据
ret3 = function3()
print(ret3['num1'])
print(ret3['num2'])
print(ret3['num3'])

# 其中: 如果return后面想要返回元组, 可以不用加 ( ) python返回多个值时, 默认就是元组格式:

def func():
    return 1, 2, 3

result = func()
print(result)
print(type(result))
