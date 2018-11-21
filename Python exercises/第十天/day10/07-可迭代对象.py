#可迭代对象:就是使用for循环遍历取值的对象就是可迭代对象
#for循环可以直接遍历取值的对象:列表,元组,字符串,集合,range
#判断对象是否是可迭代对象
from collections import Iterable
#判断对象是否是指定类型
# result = isinstance("str",int)
# print(result)
result = isinstance([1,2],Iterable)
print(result)

result = isinstance((1,2),Iterable)
print(result)

result = isinstance({"name":"lisi"},Iterable)
print(result)

result = isinstance({10,20},Iterable)
print(result)

result = isinstance(range(10),Iterable)
print(result)

#可迭代对象都有一个__iter___方法
result = dir([1,2])
print(result)


