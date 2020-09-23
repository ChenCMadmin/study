#!/usr/bin/python3

# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。%s" % (self.name, self.age, self.__weight))


# 实例化类
p = people('runoob', 10, 30)

p.speak()
# print(p.__weight)   # 报错，实例不能访问私有属性


'''
类的私有属性 和 私有方法，都不能通过对象直接访问，但是可以在本类内部访问；
类的私有属性 和 私有方法，都不会被子类继承，子类也无法访问；
私有属性 和 私有方法 往往用来处理类的内部事情，不通过对象处理，起到安全作用。
'''