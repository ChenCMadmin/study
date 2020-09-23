'''
在程序中，继承描述的是多个类之间的所属关系。
如果一个类A里面的属性和方法可以复用，则可以通过继承的方式，传递到类B里。
那么类A就是基类，也叫做父类；类B就是派生类，也叫做子类。
'''
# 父类
class A(object):
    def __init__(self):
        self.num = 10

    def print_num(self):
        print(self.num + 10)
# 子类
class B(A):
    pass

b = B()
print(b.num)
b.print_num()