import  time
import os
import logging

#获取项目的根目录
test_dir = os.path.join(os.getcwd())
# print(test_dir)

now = time.strftime('%Y-%m-%d %H_%M_%S')  # 获取当前日期
log = test_dir+'\\'+now+'_log.txt'  #日志的完整路径

'''
format 表示日志的输出格式, 参数说明:
%(levelname)s: 打印日志级别名称
%(filename)s: 打印当前执行程序名
%(lineno)d: 打印日志的当前行号
%(asctime)s: 打印日志的时间
%(message)s: 打印日志信息
'''
#filename 日志文件路径 level 日志的级别 format 输出格式
logging.basicConfig(filename=log,level=logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 日志等级从低到高的顺序是: DEBUG < INFO < WARNING < ERROR < CRITICAL
logging.debug('this is a logger debug message')     # 程序调试bug时使用
logging.info('this is a logger info message')       # 程序正常运行时使用
logging.warning('this is a logger warning message')     # 程序未按预期运行时使用，但并不是错误，如:用户登录密码错误
logging.error('this is a logger error message')     # 程序出错误时使用，如:IO操作失败
logging.critical('this is a logger critical message')   #：特别严重的问题，导致程序不能再继续运行时使用，如:磁盘空间为空，一般很少使 用


