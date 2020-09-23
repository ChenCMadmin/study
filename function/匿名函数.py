'''
匿名函数
定义:
用lambda关键词能创建小型匿名函数。这种函数省略了用def声明函数的标准步骤。

lambda表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数。
lambda函数的语法只包含一个语句，如下：
	lambda [arg1 [,arg2,.....argn]]:expression
'''

sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print("Value of total : %d" % sum( 10, 20 ))
print("Value of total : %d" % sum( 20, 20 ))

print('========1==========')
# 函数作为参数传递例如:
def func(a, b, opt):
    print('a:%d' % a)
    print('b:%d' % b)
    print('result:%d' % opt(a, b))

func(1, 2, lambda x, y : x + y)

print('========2==========')
# 作为内置函数的参数
list = [
    {"name": "zhangsan", "age": 18},
    {"name": "lisi", "age": 19},
    {"name": "wangwu", "age": 17}
]
# key:可选参数, 如果指定了该参数会使用该参数的方法进行排序。
list.sort(key = lambda x: x['name'])        #按name排序
print(list)

list.sort(key= lambda x: x['age'])      #按 age 排序
print(list)

'''
lambda函数也叫匿名函数, 即 函数没有具体的名称.
lambda x, y : x + y 中: lambda是关键字. x, y 是函数的两个形参. x + y是函数的返回值.
上面的式子可以写成:
def func( x, y ): return x + y
'''