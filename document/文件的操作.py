'''
完整的语法格式为：
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
参数说明:
file: 必需，文件路径（相对或者绝对路径）。
mode: 可选，文件打开模式
buffering: 设置缓冲
encoding: 一般使用utf8
errors: 报错级别
newline: 区分换行符
closefd: 传入的file参数类型
opener:
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
w	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
r+	打开一个文件用于读写。文件指针将会放在文件的开头。
w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
'''

f = open('./txt/test.txt', 'w')       #打开文件
f.close()       #关闭文件

f = open('./txt/test.txt', 'w', encoding = 'utf-8')
str = '''既然你诚心诚意的问了，
那我就大发慈悲的告诉你，
为了防止世界被破坏，
为了守护世界的和平，
贯彻爱与真实的邪恶，
可爱又迷人的反派角色，
白洞，白色的明天在等待着我们！
喵~就是这样 ~~~~~~'''
f.write(str)        #往文件里写入内容
f.close()

f = open('./txt/test.txt', 'r', encoding = 'utf-8')      #打开文件
print(f.read(5))    #读取文件五个字符
print('=============')
print(f.read())     # 从上次读取的位置继续读取剩下的所有的数据
f.close()

f = open('./txt/test.txt', encoding = 'utf-8')
# readlines可以按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素
content = f.readlines()
print(type(content))
for i in content :
    print(i)
f.close()

print('============')
f = open('./txt/test.txt', encoding = 'utf-8')
print(f.readline())
print(f.readline())
print(f.readline())
f.close()
