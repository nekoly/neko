my_list = [1,4,5,4]

my_tuple = (5,7)

my_set = {4,9}
#把列表转换成集合(集合不允许有重复数据,转换会去重)
result = set(my_list)
print(result)
#元组转换集合
result = set(my_tuple)
print(result)

#把列表转换成元组
result = tuple(my_list)
print(result)
#集合转换成元组
result = tuple(my_set)
print(result)

#将集合和元组转换成列表
result = list(my_set)
print(result,type(result))


result = list(my_tuple)
print(result)
#list()转换成列表
#tuple()转换成元组
#set()转换成集合,去重

