# 给函数添加一些注释, 解释说明当前函数的主要功能, 参数作用, 返回值情况.
# 给函数添加文档说明:
#
# def 函数名(a, b):
# 	'''
# 	这里可以书写该函数的主要作用
#     :param a: 第一个参数介绍
#     :param b: 第二个参数介绍
# 	:return:  返回值的介绍
# 	'''

def function(x, y) :
    '''
    该函数是两个数值相加
    :param x: 数值
    :param y: 数值
    :return: x + y
    '''
    n = x + y
    return print(n)


function(2, 1)      #调用函数

help(function)      #使用python内置函数help() 就可以发现刚刚定义的函数文档内容了