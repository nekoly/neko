#集合：以大括号形式表现的数据集合，集合里面的数据不可以重复
#集合可以根据下标获取数据，也可以添加和删除
#不可以以此种方式定义空的集合

neko_set = {1,4,"swd","neko"}

#定义一个空的集合
neko_set = set()

print(neko_set,type(neko_set))

#删除数据(删除指定数据，不能删除没有的数据）
# neko_set = {1,4,"swd","neko"}
# neko_set.remove("neko")
# print(neko_set)

#删除集合里的数据(删除没有的数据不会崩溃）
# neko_set = {1,4,"swd","neko"}
# neko_set.discard(1)
# print(neko_set)


#增加数据
#不可以增加重复的数据
# neko_set = {1,4,"swd","neko"}
# neko_set.add("ly")
# print(neko_set)

#根据下标修改数据(集合是无序的）
# neko_set[1] = 2
# print(neko_set)
neko_set = {1,4,"swd","neko"}
print(neko_set)

#取出数据容器里的每一个元素，就是遍历
for value in neko_set:
    print(value)

neko_set.add("a")
neko_set.add(234)
neko_set.add(11)
print(neko_set)

#作业：将集合转换成列表，转换成元组(三种数据容器类型相互转换）
turple(neko_set) list() set()
