#以大括号形式的键值对数据组合，{"name":"neko","age":20}
#提示一下：一般Key(99%都是字符串类型）
#不可变类型：数字 元组 可类型：变量 列表

neko_dict = {"name":"neko","age":18}
print(neko_dict,type(neko_dict))
#字典是无序（没有下标的概念）
#通过key值来取value

value = neko_dict["name"]
print(value)
#如果没有此键，使用[]会崩溃
# value = neko_dict["sex"]
# print(value)
#如果使用get的方式取值，不会崩溃
#get也可以设置字典的默认值，增加了一个元素
result = neko_dict.get("sex","female")
print(result)











