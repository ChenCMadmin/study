'''
是类对象所拥有的方法，需要用修饰器@classmethod来标识其为类方法，
对于类方法，第一个参数必须是类对象，一般以cls作为第一个参数（当然可以用其他名称的变量作为其第一个参数，但是大部分人都习惯以'cls'作为第一个参数的名字，就最好用'cls'了），能够通过实例对象和类对象去访问。
'''
class People(object):
    country = 'china'

    #类方法，用classmethod来进行修饰
    @classmethod
    def get_country(cls):
        return cls.country

    @classmethod
    def set_country(cls,country):
        cls.country = country


p = People()
print(p.get_country())   #可以用过实例对象访问
print(People.get_country())    #可以通过类访问

p.set_country('japan') #类方法还有一个用途就是可以对类属性进行修改

print(p.get_country())
print(People.get_country())


'''
从类方法和实例方法以及静态方法的定义形式就可以看出来，类方法的第一个参数是类对象cls，那么通过cls引用的必定是类对象的属性和方法；
实例方法的第一个参数是实例对象self，那么通过self引用的可能是类属性、也有可能是实例属性（这个需要具体分析），不过在存在相同名称的类属性和实例属性的情况下，实例属性优先级更高。
静态方法中不需要额外定义参数，因此在静态方法中引用类属性的话，必须通过类实例对象来引用
python中的方法总结:
    1.实例方法(对象方法) --> 场景很多
        调用格式: 对象名.实例方法名()
        使用场景: 在方法中需要self
        
    2.类方法 --> 对私有类属性取值或者赋值
        定义格式: @classmethod
                 def 类方法名(cls):
        调用格式: 类名.类方法名()  或者 对象名.类方法名()
        使用场景: 在方法中需要cls类名
        
    3.静态方法 --> 一般不用
        定义格式: @staticmethod
                 def 静态方法名():
        调用格式: 类名.类方法名() 
        使用场景: 在方法中不需要self 也不需要cls       
'''