'''
如果需要修改一个对象的属性值，通常有2种方法
对象名.属性名 = 数据 ----> 直接修改
对象名.方法名() ----> 间接修改
私有属性不能直接访问，所以无法通过第一种方式修改，
一般的通过第二种方式修改私有属性的值：定义一个可以调用的公有方法，在这个公有方法内访问修改。
'''

class Prentice(object):
    def __init__(self):
        # 私有属性，可以在类内部通过self调用，但不能通过对象访问
        self.__money = 10000

    # 现代软件开发中，通常会定义get_xxx()方法和set_xxx()方法来获取和修改私有属性值。
    # 返回私有属性的值
    def get_money(self):
        return self.__money

    # 接收参数，修改私有属性的值
    def set_money(self, num):
        print('原本的私有属性：%d'%self.__money)
        self.__money = num

damao = Prentice()
# 对象不能访问私有权限的属性和方法
# print(damao.__money)

# 可以通过访问公有方法set_money()来修改私有属性的值
damao.set_money(100)

# 可以通过访问公有方法get_money()来获取私有属性的值
print(damao.get_money())