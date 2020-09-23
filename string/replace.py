'''
Python replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
replace()方法语法：
	str.replace(old, new[, max])
old -- 将被替换的子字符串。

new -- 新字符串，用于替换old子字符串。

max -- 可选字符串, 替换不超过 max 次

'''

name = 'hello world ha ha ha'
name1 = name.replace("ha", "Ha")
print(name1)
name2 = name.replace("ha", "Ha", 1)
print(name2)