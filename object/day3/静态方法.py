'''需要通过修饰器@staticmethod来进行修饰，静态方法不需要多定义参数，可以通过对象和类来访问。'''
class People(object):
    country = 'china'

    @staticmethod
    #静态方法
    def get_country():
        return People.country


p = People()
# 通过对象访问静态方法
# p.get_contry()  #报错

# 通过类访问静态方法
print(People.get_country())