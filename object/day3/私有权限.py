class Master(object):
    def __init__(self):
        self.kongfu = "古法煎饼果子配方"
    def make_cake(self):
        print("[古法] 按照 <%s> 制作了一份煎饼果子..." % self.kongfu)

class School(object):
    def __init__(self):
        self.kongfu = "现代煎饼果子配方"

    def make_cake(self):
        print("[现代] 按照 <%s> 制作了一份煎饼果子..." % self.kongfu)

class Prentice(School, Master):
    def __init__(self):
        self.kongfu = "猫氏煎饼果子配方"
        # 私有属性，可以在类内部通过self调用，但不能通过对象访问
        self.__money = 10000

    # 私有方法，可以在类内部通过self调用，但不能通过对象访问
    def __print_info(self):
        print(self.kongfu)
        print(self.__money)

    def make_cake(self):
        self.__init__()
        print("[猫氏] 按照 <%s> 制作了一份煎饼果子..." % self.kongfu)

    def make_old_cake(self):
        Master.__init__(self)
        Master.make_cake(self)


    def make_new_cake(self):
        School.__init__(self)
        School.make_cake(self)

class PrenticePrentice(Prentice):
    pass


damao = Prentice()
# 对象不能访问私有权限的属性和方法
print(damao.__money)
damao.__print_info()


pp = PrenticePrentice()
# 子类不能继承父类私有权限的属性和方法
print(pp.__money)
pp.__print_info()

'''
Python中没有像C++中 public 和 private 这些关键字来区别公有属性和私有属性。
Python是以属性命名方式来区分，如果在属性和方法名前面加了2个下划线'__'，则表明该属性和方法是私有权限，否则为公有权限。
'''