'''

运算符	描述	                                        示例
==	检查两个操作数的值是否相等，如果是则条件变为真。	如a=3,b=3，则（a == b) 为 True
!=	检查两个操作数的值是否相等，如果值不相等，则条件变为真。	如a=1,b=3，则(a != b) 为 True
>	检查左操作数的值是否大于右操作数的值，如果是，则条件成立。	如a=7,b=3，则(a > b) 为 True
<	检查左操作数的值是否小于右操作数的值，如果是，则条件成立。	如a=7,b=3，则(a < b) 为 False
>=	检查左操作数的值是否大于或等于右操作数的值，如果是，则条件成立。	如a=3,b=3，则(a >= b) 为 True
<=	检查左操作数的值是否小于或等于右操作数的值，如果是，则条件成立。	如a=3,b=3，则(a <= b) 为 True

'''

a = 10
b = 20
print(a==b)

'''

运算符	逻辑表达式	描述	                                                            实例
and	    x and y	    布尔"与"：如果 x 为 False，x and y 返回 False，否则它返回 y 的值。	  True and False， 返回 False。
or	    x or y	    布尔"或"：如果 x 是 True，它返回 True，否则它返回 y 的值。	          False or True， 返回 True。
not	    not x	    布尔"非"：如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	  not True 返回 False, not False 返回 True

'''

a = 10
b = 20

if a > 0 and b > 10:
    print('对')
else:
    print('错')


