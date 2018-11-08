#for循环最经常的使用方式就是遍历（所有容器类型）
#获取所有容器类型里面的的元素，就是遍历（字符串，列表，元组，字典，集合）

#遍历字符串
str = "abc"
for value in str:
    print(value)
print("------------------------")
#列表
my_list = ["swd","neko","nekoswd"]
for value in my_list:
    print(value)
print("------------------------")
#把列表当中的元素都遍历出来，还想对应的下标

neko_list = enumerate(["boy","girl","neko"])
# for value in neko_list:
#     # print(value)
#     print(value,type)

#拆包：获取容器类型中所有元素和所有下标
for index,value in neko_list:
    print(index,value)
print("-------------------------")

#遍历元组
for value in enumerate(("neko","swd",8,65)):
    print(value)
print("-------------------------")
#字典遍历（json:字典）默认遍历出来的是key
neko_dict = {"name":"swd","age":17}
for value in neko_dict:
    print(value)

#遍历value
for value in neko_dict.values():
    print(value)

#将key和value全都遍历出来
# for key,value in neko_dict():
#     print(key,value)
print("---------------------")
#集合
my_set = {1,3,5}
for value in my_set:
    print(value)
