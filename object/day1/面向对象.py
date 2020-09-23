'''
面向对象定义类
定义一个类，格式如下：
class 类名:
    方法列表
demo：定义一个Hero类

# 经典类（旧式类）定义形式:
# class Hero:
# class Hero():

# 新式类定义形式:
class Hero(object):
    def info(self):
        print("英雄各有见，何必问出处。")
说明：
定义类时有2种形式：新式类和经典类，上面代码中的Hero为新式类，前两行注释部分则为经典类；
object 是Python 里所有类的最顶级父类；
类名 的命名规则按照"大驼峰命名法"；
info 是一个实例方法，第一个参数一般是self，表示实例对象本身，当然了可以将self换为其它的名字，其作用是一个变量 这个变量指向了实例对象
'''

class Hero(object):  # 新式类定义形式
    """info 是一个实例方法，类对象可以调用实例方法，实例方法的第一个参数一定是self"""
    def info(self):
        """当对象调用实例方法时，Python会自动将对象本身的引用做为参数，
            传递到实例方法的第一个参数self里"""
        print(self)
        print("self各不同，对象是出处。")


# Hero这个类 实例化了一个对象  taidamier(泰达米尔)
taidamier = Hero()

# 对象调用实例方法info()，执行info()里的代码
# . 表示选择属性或者方法
taidamier.info()

print(taidamier)  # 打印对象，则默认打印对象在内存的地址，结果等同于info里的print(self)
print(id(taidamier))  # id(taidamier) 则是内存地址的十进制形式表示




