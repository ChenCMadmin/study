# 定义一个Master类
class Master(object):
    def __init__(self):
        # 属性
        self.kongfu = "古法煎饼果子配方"

    # 实例方法
    def make_cake(self):
        print("按照 <%s> 制作了一份煎饼果子..." % self.kongfu)


# 定义Prentice类，继承了 Master，则Prentice是子类，Master是父类。
class Prentice(Master):
 #子类可以继承父类所有的属性和方法，哪怕子类没有自己的属性和方法，也可以使用父类的属性和方法。
    pass

# laoli = Master()
# print(laoli.kongfu)
# laoli.make_cake()

damao = Prentice()  # 创建子类实例对象
print(damao.kongfu) # 子类对象可以直接使用父类的属性
damao.make_cake()   # 子类对象可以直接使用父类的方法

'''
子类在继承的时候，在定义类时，小括号()中为父类的名字
父类的属性、方法，会被继承给子类
'''