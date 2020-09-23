'''

Python 中 while 语句的一般形式：
while 判断条件(condition)：
    执行语句(statements)……

无限循环
我们可以通过设置条件表达式永远不为 false 来实现无限循环

在 while … else 在条件语句为 false 时执行 else 的语句块。
while <expr>:
    <statement(s)>
else:
    <additional_statement(s)>

'''
x = 1
i = 1
y = 1

while x < 5 :
    print('好了')
    x += 1

while True :   # 死循环
    i += 1
    if i == 10 :
        print('结束')
        break          # break 语句用于跳出当前循环体

while y < 5 :
    y += 1
    print('匹配到')
else :
    print('没有匹配')

'''
while和if的用法基本类似，区别在于：

​	if 条件成立，则执行一次；

​	while 条件成立，则重复执行，直到条件不成立为止。

一般情况下，需要多次重复执行的代码，都可以用循环的方式来完成

循环不是必须要使用的，但是为了提高代码的重复使用率，所以有经验的开发者都会采用循环

不可以停止的循环(判断条件一直满足) 称之为死循环, 在开发中我们应该尽量防止死循环,因为死循环太浪费设备性能.

while循环内部的代码需要进行缩进,python对缩进要求非常严格.
'''

