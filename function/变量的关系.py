# 相同名字的全局和局部变量
# 当函数内出现局部变量和全局变量相同名字时，函数内部中的 变量名 = 数据 此时理解为定义了一个局部变量，而不是修改全局变量的值

# 定义一个全局变量
a = 100

def func1():
    a = 300
    print('------func1----修改前---a = %d ' % a)
    a = 200
    print('------func1----修改后---a = %d ' % a)

def func2():
    print('------func2-----a = %d ' % a)

# 调用函数
func1()
func2()

print('=====================')
# 修改全局变量
# 如果在函数中出现global 全局变量的名字 那么这个函数中即使出现和全局变量名相同的变量名 = 数据 也理解为对全局变量进行修改，而不是定义局部变量

# 定义一个全局变量
a = 100

def func1():
    global a
    print('------func1----修改前---a = %d ' % a)
    a = 200
    print('------func1----修改后---a = %d ' % a)

def func2():
    print('------func2-----a = %d ' % a)

# 调用函数
func1()
func2()

'''
如果在一个函数中需要对多个全局变量进行修改，那么可以使用
# 可以使用一次global对多个全局变量进行声明
global a, b
     
# 还可以用多次global声明都是可以的
global a
global b
'''