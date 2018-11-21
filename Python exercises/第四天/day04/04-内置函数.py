#内置函数:可以直接使用的函数(不需要自己声明,python已经定义好了)
#print,len,max,min,sort,sorted,open
#api(接口)
#len 可以统计容器类型的长度(个数)(字符串,列表,元组,字典,集合)
#统计字符串的个数
str = "abc"
result = len(str)
print(result)
#列表
result = len(["a","b"])
print(result)
#字典
result = len({"a":"b"})
print(result)
#max函数 统计容器类型数据中的最大值
result = max("13100")
print(result)

#列表
result = max([5,10,100])
print(result)
#min统计容器类型数据中的最小值
result = min([10,20,30])
print(result)

#列表排序(会返回一个新的列表)
new_list = sorted([8,6,7],reverse=True)
print(new_list)
#删除变量
del new_list
# print(new_list)

