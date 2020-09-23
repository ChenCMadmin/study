class F1(object):
    def show(self):
        print('F1.show')

class S1(F1):
    def show(self):
        print('S1.show')

class S2(F1):
    def show(self):
        print('S2.show')

def Func(obj):
    # python是弱类型，即无论传递过来的是什么，obj变量都能够指向它，这也就没有所谓的多态了（弱化了这个概念）
    print(obj.show())

s1_obj = S1()
Func(s1_obj)

print('=============')

s2_obj = S2()
Func(s2_obj)

'''
Python的多态，就是弱化类型，重点在于对象参数是否有指定的属性和方法，如果有就认定合适，而不关心对象的类型是否正确。
定义obj这个变量是说的类型是：F1的类型，但是在真正调用Func函数时给其传递的不一定是F1类的实例对象，有可能是其子类的实例对象， 这种情况就是所谓的多态
'''