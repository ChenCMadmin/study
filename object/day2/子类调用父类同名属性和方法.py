class Master(object):

    def make_cake(self):
        print("按照 [古法] 制作了一份煎饼果子...")


class School(object):

    def make_cake(self):
        print(" 按照 [现代] 制作了一份煎饼果子...")

# 自定义类
class Master(object):
    # 实例方法
    def make_cake(self):
        print("按照 [古法] 制作了一份煎饼果子...")

# 自定义类
class School(object):

    def make_cake(self):
        print("按照 [现代] 制作了一份煎饼果子...")


# 多继承，继承了多个父类
class Prentice(School, Master):

    # 实例方法
    def make_cake(self):
        print("按照 [猫氏] 制作了一份煎饼果子...")

    # 调用父类方法格式：父类类名.父类方法(self)
    def make_old_cake(self):

        # 调用父类Master的实例方法
        Master.make_cake(self)

    def make_new_cake(self):

        # 调用父类School的实例方法
        School.make_cake(self)

# 实例化对象，自动执行子类的__init__方法
damao = Prentice()

damao.make_cake() # 调用子类的方法（默认重写了父类的同名方法）

print("--" * 10)
damao.make_old_cake() # 进入实例方法去调用父类Master的方法

print("--" * 10)
damao.make_new_cake() # 进入实例方法去调用父类School的方法

print("--" * 10)
damao.make_cake() # 调用本类的实例方法

'''

'''