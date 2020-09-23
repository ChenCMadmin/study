# 定义一个字典
my_dict = {"name": "小红", "age": 22, "no": "009"}

# # 遍历-key
# for key in my_dict.keys():
#     print(key)
#
# # 遍历value
# for value in my_dict.values():
#     print(value)
#
# # 遍历items
# for item in my_dict.items():
#     print(item[0])
#     print(item[1])


# 通过设置两个临时变量
print(my_dict.items())
for key, value in my_dict.items():
    print("key:", key)
    print("value:", value)