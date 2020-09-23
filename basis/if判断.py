'''
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
如果 "condition_1" 为 True 将执行 "statement_block_1" 块语句
如果 "condition_1" 为False，将判断 "condition_2"
如果"condition_2" 为 True 将执行 "statement_block_2" 块语句
如果 "condition_2" 为False，将执行"statement_block_3"块语句
'''

x = 9
if 0 < x < 20 :
    print('少年')
elif 20 <= x < 40 :
    print('青年')
else:
    print('老年')


'''

操作符	描述
<	    小于
<=	    小于或等于
>	    大于
>=	    大于或等于
==	    等于，比较两个值是否相等
!=	    不等于

'''

'''
if 表达式1:
    语句
    if 表达式2:
        语句
    elif 表达式3:
        语句
    else:
        语句
elif 表达式4:
    语句
else:
    语句
'''

if 0 < x < 20:
    if 0 < x < 5:
        print('幼儿')
    elif 5 < x < 10:
        print('儿童')
    else:
        print('少年')
elif 20 <= x < 40:
    print('青年')
else:
    print('老年')
