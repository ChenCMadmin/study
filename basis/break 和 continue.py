'''
break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
'''


for i in range(5):
    if i == 2 :
        break             #跳出循环，循环结束
    print('*********')

for i in range(5):
    if i == 2 :
        print('继续')
        continue          #跳出当前循环，循环继续
    print('=========')

'''
break/continue只能用在循环中，除此以外不能单独使用

break/continue在嵌套循环中，只对最近的一层循环起作用

continue是结束单次循环,break是结束整个循环,注意对比记忆
'''