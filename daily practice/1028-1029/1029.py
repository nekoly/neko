# age_man = int(input("input your age"))
#
# if  age_man >0 and age_man < 18:
#
#     print("小屁孩 ")
# elif age_man >= 18 and age_man <= 22:
#     print("小朋友")
# elif age_man > 22 and age_man <= 28:
#     print("小鲜肉")
# elif age_man >= 28 and age_man <= 35:
#     print("中青年")
# else:
#     print("老男人")

#格式化符号：%s,%d,%f,%x
#%s：输出字符串
#%f:输出float类型
#%d：输出int类型
#%x:输出16进制的类型

name = "neko"
print("my name is %s" % name)

score = 100
print("yr number is %d" %score)

pi = 3.1415926
#%f默认保留6位数字，会四舍五入；
print("圆周率%.2f" % pi)

num = 19
print("%x" %num)

#元组：以小括号形式的数据结合，（1，2，3，“abc",True)
#可以存储任意数据类型
#注意：元组可以根据下标获取数据，但是不能对元组进行数据修改
# neko_tuple = (1,8,"abc",True,2.3)
# print(neko_tuple,type(neko_tuple))

#根据下标取值
# value = neko_tuple[-1]
# print(value)
#元组不能根据下标删除数据

#修改数据
# del neko_tuple[2]
# print(neko_tuple)
#注意：不论元组里面装了什么数据类型都不可以修改
neko_tuple = (2,[4,5])
neko_list = neko_tuple[1]
print(neko_list)
neko_list = [1,2]
print(neko_list)

#修改元素
ly_list = [23,"数据中心","流量一部","大客户部","物流中心"]
ly_list[0] = "neko"
print(ly_list)

#删除列表中的元素
#删除指定数据
ly_list.remove("物流中心")
print(ly_list)

#根据下标删除元素(不能列表越界，删除的下标要合法）

del ly_list[1]
print(ly_list)

#使用pop方式删除数据(pop如果不传任何参数，默认删除最后一个）
#将删除的数据返回给我们
result = ly_list.pop()
print(ly_list,result)

#判断指定数据是否在列表当中
result = "neko" in ly_list
print(result)
result = ly_list.index("流量一部")
print(result)

#根指定数据获取数据在列表中的个数
l_list = [6,6,6,4,3,5,7,8,6]
result = l_list.count(6)
print(result)









































