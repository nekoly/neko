#元组：以小括号形式的数据结合,(1,2,"abc",True)
#可以存储任意数据类型
#注意：元组可以根据下标获取数据，但是不能对元组进行数据修改

# neko_tuple = (5,23,"ly",True,4.6)
# print(neko_tuple,type(neko_tuple))
#
# #根据下标取值
#
# value = neko_tuple[-1]
# print(value)

#元组不能根据下标删除数据
# del neko_tuple[3]
# print(neko_tuple)

#修改数据
# neko_tuple[0] = 3
# print(neko_tuple)
#注意不论元组里面装什么数据类型都不可以修改
neko_tuple = (1,[2,3])
#neko_tuple[1] = [2,3]
neko_list = neko_tuple[1]
print(neko_list)
neko_list = [1,2]
print(neko_tuple)

#定义一个空的元组
#如果定义的元组，只有一个元素，那么元组的类型为元素的类型
#如果指定只传一个元素，还想保证是元组类型，需要加上逗号
neko_tuple = (1,)
print(neko_tuple,type(neko_tuple))

#判断数据是否在元组里

neko_tuple = (10,10,5,19,34)
result = 5 in neko_tuple
print(result)
result = 3 not in neko_tuple
print(result)

#获取元组中元素的下标（字符串,列表，元组都有下标，有序的）

result = neko_tuple.index(5)
print(result)

#元组中元素的个数
result = neko_tuple.count(10)
print(result)
























