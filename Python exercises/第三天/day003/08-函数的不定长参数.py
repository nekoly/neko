#函数的不定长参数:1.不定长位置参数2,不定长关键字参数

#不定参数:调用函数的时候不确定传入多少个参数
#可能是0个或者多个

#--------------不定长位置参数的定义及调用--------------
#*args代表不定长位置参数,约定俗称起的名字
def sum_num(*args):
	#提示:args:会把调用函数传入的位置参数封装到一个元组里面
	print(args,type(args))

	#计算结果变量
	result = 0
	for value in args:

		result += value
	return result


result = sum_num(1,2,3,4,6,8)
print(result)
# sum_num(a=1,b=2)

#------------不定长关键字子参数函数的定义及调用-------
#**kwargs 代表不定位置参数
def show_msg(**kwargs):

	print(kwargs,type(kwargs))

	for key,value in kwargs.items():

		print(key,value)

#调用不定长位置参数的函数
show_msg(a=1,b=2)
#使用位置参数的方式调用不定长关键字参数的函数
# show_msg(1,2)

# def pachong():
# 	#1.232323
# 	data = "asdasd"
# 	return data
#
#
# data = pachong()
# print(data)
#爬虫:只能抓取用户有权限能看见的数据