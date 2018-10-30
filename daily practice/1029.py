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











































