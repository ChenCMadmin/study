'''
os模块中的rename()可以完成对文件的重命名操作
格式:
import os
os.rename(需要修改的文件名, 新的文件名)
'''

import os

# os.rename('./test/test2.txt', './test/test_3.txt')    #重命名文件

#os.remove('./test/test_1.txt')   #删除文件

# os.mkdir('./test/test_1')   #创建文件夹

os.chdir("./")    #改变当前文件的默认路径   ./ 或者../ 都是相对路径

print(os.getcwd())  #获取当前目录

print(os.listdir("./test"))     #获取目录列表

# os.rmdir("./test/test_1")    #删除文件夹


import os
# 应用
# # 准备工作批量建文件
# # 01 当前目录下创建一个文件夹
# os.mkdir("test1")
#
# # 02 指定默认目录
# os.chdir("test1")
# print(os.getcwd())
#
# # 03 在test下面创建10个文件
# for i in range(1, 11):
#     # 打开文件
#     f =open("hm%d.txt" % i, "w")
#     # 关闭文件
#     f.close()

# 实际工作批量修改文件
# hmx.txt -> hmx[中国].txt

# 01 指定默认目录
os.chdir("test1")

# 02 获取当前目录下的目录列表
my_list = os.listdir()

# 03 遍历my_list
for file_name in my_list:
    # 得的新的文件名:replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)
    new_file_name = file_name.replace(".txt", "[中国].txt")
    # 对文件重命名
    os.rename(file_name, new_file_name)