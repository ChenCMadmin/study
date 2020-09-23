# 删除元素
# 对字典进行删除操作，有一下几种：del  clear()

my_dict = {'name':'班长', 'id':100, 'sex':'f', 'address':'地球亚洲中国北京'}

del my_dict['id']   #del删除指定的元素
print(my_dict)

my_dict.clear()     #clear清空整个字典
print(my_dict)


