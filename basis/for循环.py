'''
Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
for循环的一般格式如下：

for <variable> in <sequence>:
    <statements>
else:
    <statements>
'''


list = [1, 2, 3, 4,]
for i in list:
    if i == 3:
        print('对')
else:
    print('结束---------')

'''函数语法
range(start, stop[, step])
参数说明：
start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
'''

for i in range(len(list)):
    print(i)

for i in range(3, 5):  # 左闭右开
    print(i)

# range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):
for i in range(2, 8, 2):
    print(i)


'''
for循环后面可以跟随一个else.构成for......else句式: (也可以不要else,具体看需求)

for 临时变量 in 列表或者字符串等可迭代对象:
    将会执行的语句
else:
    for循环执行完毕之后,会执行调用的语句
for循环中的"临时变量" 的作用范围仅仅是当前for循环体中缩进的区域

for循环判断的条件依然是 for 后面的条件是否为True,为True则可以进入,否则不允许进入循环体.

for循环中的in是个关键字 写for循环的时候不能够去掉in
'''