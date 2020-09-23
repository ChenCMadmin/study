class Master(object):
    def __init__(self):
        # 实例变量，属性
        self.kongfu = "古法煎饼果子配方"

    # 实例方法，方法
    def make_cake(self):
        print("[古法] 按照 <%s> 制作了一份煎饼果子..." % self.kongfu)

    def dayandai(self):
        print("师傅的大烟袋..")

class School(object):
    def __init__(self):
        self.kongfu = "现代煎饼果子配方"

    def make_cake(self):
        print("[现代] 按照 <%s> 制作了一份煎饼果子..." % self.kongfu)

    def xiaoyandai(self):
        print("学校的小烟袋..")

# 多继承，继承了多个父类（School在前）
class Prentice(School, Master):
    pass

# damao = Prentice()
# print(damao.kongfu)
# damao.make_cake()
# damao.dayandai()
# damao.xiaoyandai()


class Prentice(Master, School):  # 多继承，继承了多个父类（Master在前）
    pass

damao = Prentice()
# 执行Master的属性
print(damao.kongfu)
# 执行Master的实例方法
damao.make_cake()

# 重名不受影响
damao.dayandai()
damao.xiaoyandai()

# 子类的魔法属性__mro__决定了属性和方法的查找顺序
print(Prentice.__mro__)

'''
多继承可以继承多个父类，也继承了所有父类的属性和方法
注意：如果多个父类中有同名的 属性和方法，则默认使用第一个父类的属性和方法（根据类的魔法属性mro的顺序来查找）
多个父类中，重名的属性和方法，不会有任何影响。
'''