'''
一个函数里面又调用了另外一个函数，这就是所谓的函数嵌套调用
如果函数A中，调用了另外一个函数B，那么先把函数B中的任务都执行完毕之后才会回到上次 函数A执行的位置
一个函数中可以嵌套无数个函数.
函数可以连着进行嵌套, 即 a函数嵌套于 b函数, b函数又嵌套于 c函数, c函数又.......
'''

def funcB():
    print('---- testB start----')
    print('这里是testB函数执行的代码...(省略)...')
    print('---- testB end----')

def funcA():
    print('---- testA start----')
    funcB()
    print('---- testA end----')

funcA()
