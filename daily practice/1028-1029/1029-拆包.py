#拆包：就是把容器类型（字符串，列表，元组，字典，集合）
#每一个数据都用变量保存一下
#字符串
neko_str = "abc"
a,b,c = neko_str
print(a,b,c)

#列表
neko_list = [2,4]
num1,num2 = neko_list
print(num1,num2)

#元组
neko_tuple = (2,6)
num1,num2 = neko_tuple
print(num1,num2)

#拆字典
neko_dict = {"name":"neko","age":20}.value()
a,b = neko_dict
print(a,b)

#集合
neko_set = {3,5}
num1,num2 = neko_set
print(num1,num2)