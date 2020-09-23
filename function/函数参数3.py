# *args: 表示 将位置参数中的剩余实参存放到 args 中, 且以元组的形式保存
def foo(x, *args):
    print(x)
    print(args)

foo(1, 2, 3, 4, 5)  # 其中的2,3,4,5都给了args

def foo(x, y=1, *args):
    print(x)
    print(y)
    print(args)

foo(1, 2, 3, 4, 5)  # 其中的x为1，y=1的值被2重置了，3,4,5都给了args


def foo(x, *args, y=1):
    print(x)
    print(args)
    print(y)

foo(1, 2, 3, 4, 5)  # 其中的x为1，2,3,4,5都给了args,y按照默认参数依旧为1

print('===========================')

# ** kwargs: 表示 形参中按照关键字传值 把多余的值以字典呈现
def foo(x, **kwargs):
    print(x)
    print(kwargs)

foo(1, y=1, a=2, b=3, c=4)  # 将y=1,a=2,b=3,c=4以字典的方式给了kwargs

def foo(x,*args,**kwargs):
    print(x)
    print(args)
    print(kwargs)
foo(1,2,3,4,y=1,a=2,b=3,c=4)#将1传给了x，将2,3,4以元组方式传给了args，y=1,a=2,b=3,c=4以字典的方式给了kwargs

# 位置参数、默认参数、**kwargs三者的顺序必须是位置参数、默认参数、**kwargs，不然就会报错
def foo(x,y=1,**kwargs):
    print(x)
    print(y)
    print(kwargs)
foo(1,a=2,b=3,c=4)#将1按照位置传值给x，y按照默认参数为1，a=2,b=3,c=4以字典的方式给了kwargs