
'''
Python字符串运算符
下表实例变量 a 值为字符串 "Hello"，b 变量值为 "Python"：

操作符	描述	                         实例
+	    字符串连接	                            a + b 输出结果： HelloPython
*	    重复输出字符串	                         a*2 输出结果：HelloHello
[]	    通过索引获取字符串中字符	                a[1] 输出结果 e
[ : ]	截取字符串中的一部分，遵循左闭右开原则，str[0:2] 是不包含第 3 个字符的。 	a[1:4] 输出结果 ell
in	    成员运算符 - 如果字符串中包含给定的字符返回 True	                        'H' in a 输出结果 True
not in	成员运算符 - 如果字符串中不包含给定的字符返回 True	                        'M' not in a 输出结果 True
r/R	    原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。
 原始字符串除在字符串的第一个引号前加上字母 r（可以大小写）以外，与普通字符串有着几乎完全相同的语法。	
                                                                        print( r'\n' )
                                                                        print( R'\n' )

'''

str = 'abcdefg'
str1 = 'hopq'
print(str[0:2])
print(str + str1)


# Python 的字符串内建函数
# 定义一个字符串
a = "abcdef"

# <1>find
# find()方法语法：
# 	str.find(str, beg=0, end=len(string))
#获取对应字符串的下标索引
#如果查询到对应的字符串 会返回一个下标索引
#如果没有查询到 会返回一个-1
ret1 = a.find("cdd")
print(ret1)

# <2>index
# 跟find()方法一样，只不过如果str不在 mystr中会报一个异常.
# ret2 = a.index("cdd")
# print(ret2)

# <3>count
# 返回 str在start和end之间 在 mystr里面出现的次数
ret3 = a.count("q")
print(ret3)

# <4>replace
# 把 mystr 中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次.
ret4 = a.replace("a", "w")
print(ret4)
print(a)

# 5>split
# 以 str 为分隔符切片 mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串
ret5 = a.split("ad")
print(ret5)

#可以使用count来判断下字符的个数 如果字符的个数大于0 存在index
count = a.count("a")
#如果大于0
if count > 0:
    index = a.index("a")
    print(index)
# 定义一个字符串
a = "abcAef"

# <6>capitalize
# 把字符串的第一个字符大写
ret1 = a.capitalize()
print(ret1)
print(a)

# <7>title
# 把字符串的每个单词首字母大写
ret2 = a.title()
print(ret2)

# <8>startswith
# 检查字符串是否是以 hello 开头, 是则返回 True，否则返回 False
ret3 = a.startswith("abca")
print(ret3)

# <9>endswith
# 检查字符串是否以obj结束，如果是返回True,否则返回 False.
ret4 = a.endswith(".MP4")
print(ret4)

# <10>lower
# 转换 mystr 中所有大写字符为小写
ret5 = a.lower()
print(ret5)

# <11>upper
# 转换 mystr 中的小写字母为大写
ret6 = a.upper()
print(ret6)
# 定义一个字符串
a = "   2222abcd33333"
# <12>ljust
# 返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
ret1 = a.ljust(10, "1")
print(ret1)

# <13>rjust
# 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
ret2 = a.rjust(10, "1")
print(ret2)

# <14>center
# 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
ret3 = a.center(10, "2")
print(ret3)

# <15>lstrip
# 删除 mystr 左边的空白字符(无论是空格 还是\n 或者是\t)
# \t 就是 键盘上的tab键
print(a)
ret4 = a.lstrip("2")
print(ret4)

# <16>rstrip
# 删除 mystr 字符串末尾的空白字符
ret5 = a.rstrip("3")
print(ret5)

# <17>strip
# 删除mystr字符串两端的空白字符
ret6 = a.strip(" 3")
print(ret6)
# 定义一个字符串
a = "acbdf"

# <18>rfind
# 类似于 find()函数，不过是从右边开始查找.
# 从左侧到右侧查找
ret1 = a.find("b")
print(ret1)
ret1 = a.rfind("b")
print(ret1)


# <19>rindex
# 类似于 index()，不过是从右边开始. 异常


# <20>partition 开发中使用
# 把mystr以str分割成三部分,str前，str和str后
ret2 = a.partition("c")
print(type(ret2))
print(ret2)

# <21>rpartition
# 类似于 partition()函数,不过是从右边开始.
ret3 = a.rpartition("c")
print(ret3)

# 定义一个字符串
a = "      "

# <22>splitlines
# 按照行分隔，返回一个包含各行作为元素的列表
ret1 = a.splitlines()
print(ret1)


# <23>isalpha
# 如果 mystr 所有字符都是字母 则返回 True,否则返回 False
ret2 = a.isalpha()
print(ret2)


# <24>isdigit
# 如果 mystr 只包含数字则返回 True 否则返回 False.
ret3 = a.isdigit()
print(ret3)

# <25>isalnum
# 如果 mystr 所有字符都是字母或数字则返回 True,否则返回 False
ret4 = a.isalnum()
print(ret4)


# <26>isspace
# 如果 mystr 中只包含空格，则返回 True，否则返回 False.
ret5 = a.isspace()
print(ret5)


# <27>join
# mystr 中每个元素后面插入str,构造出一个新的字符串
# 定义一个变量 记录列表
my_list = ["1", "x", "hello"]

# 最终打印出来一个字符串为 100x00hello
ret6 = "00".join(my_list)
print(ret6)


# __________________________________________
my_str = "    ab cd    "
# # 最终结果为abcd
ret = my_str.replace(" ", "")
print(ret)
ret2 = my_str.split()
print(ret2)
ret3 = "".join(ret2)
print(ret3)
# 内置函数help
# 对字符串不了解 不知道他有什么特点 有哪些方法
# 或者对他的方法不熟悉
my_str = "hello"
print(type(my_str))
# 查找
help(str.lower)
# 如果查看一个类的所有方法
# 首先要确定他的类型 -> type(数值) <class "类型">
# help(类型)
# 如果查看这个类型的指定的方法
# help(类型.方法名)


'''
字符串是 Python 中最常用的数据类型。我们可以使用引号('或")来创建字符串。

创建字符串很简单，只要为变量分配一个值即可。例如：var1 = 'Hello World!'

Python不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。

Python访问子字符串，可以使用方括号来截取字符串

你可以对已存在的字符串进行修改，并赋值给另一个变量, 字符串不支持修改.

Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。

python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。

三引号的语法是一对连续的单引号或者双引号（通常都是成对的用）。
'''