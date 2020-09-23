# 自定义类
class Master(object):

    # 实例方法，方法
    def make_cake(self):
        print("按照 [古法] 制作了一份煎饼果子...")


# 父类是 Master类
class School(Master):

    # 实例方法，方法
    def make_cake(self):
        print("按照 [现代] 制作了一份煎饼果子...")
        # 执行父类的实例方法
        super().make_cake()


# 父类是 School 和 Master
# 多继承，继承了多个父类
class Prentice(Master ,School):
    # 实例方法，方法
    def make_cake(self):
        print("按照 [猫氏] 制作了一份煎饼果子...")

    def make_all_cake(self):

        # 方式1. 指定执行父类的方法（代码臃肿）
        # School.make_cake(self)
        # Master.make_cake(self)

        # 方法2. super() 带参数版本，只支持新式类
        # super(Prentice, self).make_cake()
        # self.make_cake()

        # 方法3. super()的简化版，只支持新式类
        # 执行父类的 实例方法
        super().make_cake()


damao = Prentice()
damao.make_cake()
damao.make_all_cake()

# print(Prentice.__mro__)

'''
子类继承了多个父类，如果父类类名修改了，那么子类也要涉及多次修改。而且需要重复写多次调用，显得代码臃肿。
使用super() 可以逐一调用所有的父类方法，并且只执行一次。调用顺序遵循 mro 类属性的顺序。
注意：如果继承了多个父类，且父类都有同名方法，则默认只执行第一个父类的(同名方法只执行一次，目前super()不支持执行多个父类的同名方法)
super() 在Python2.3之后才有的机制，用于通常单继承的多层继承。
'''