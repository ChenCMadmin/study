# open 打开文件有多种模式，下面是常见的4种
# r：读数据，默认模式
# w：写数据，如果已有数据则会先清空
# a：向文件末尾追加数据
# x : 写数据，如果文件已存在则失败
# 第2至4种模式如果第一个参数指定的文件不存在，则会先创建一个空文件
# encoding: 一般使用utf8
# newline: 区分换行符

import csv

list = []
# 打开csv参数文件
with open('../txt/shcode.csv', 'r', encoding='utf-8') as f:
    reads = csv.reader(f)
    for i in reads:
        # 设置写入文件格式
        list1= []
        list1.append('{|symbol|: |SH.%s|, |dataType|:|6|,|length|:10,|order|:|null|,|start|:0,|end|:0,|isJson|:false}/'%i[0])
        # 新的文件格式加入列表
        # print(list1)
        list.append(list1)

# 列表数据写入新的csv文件中
with open('../txt/code.txt', 'a', encoding='utf-8',newline='') as h:
    writer = csv.writer(h)
    # 写入多行数据
    writer.writerows(list)

