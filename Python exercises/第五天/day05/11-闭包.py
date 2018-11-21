#闭包:闭包本质上也是一个函数(高阶函数)
#在函数嵌套的前提下,内部函数使用了外部函数的参数或者变量
#并且把这个内部函数返回,那么返回的函数就叫做闭包
# def show(msg):
# 	#外部的变量
# 	num = 10
# 	def inner():
# 		#打印外部的变量,msg外部的变量
# 		#既使用了外部函数的参数,又使用了外部函数的变量
# 		print(msg,num)
# 	#inner他就是闭包
# 	return inner
# #new_func就是inner,就是闭包
# new_func = show("哈哈")
# # print(new_func)
# #调用闭包
# new_func()
# #闭包的应用场景:可以根据参数生成不同的返回函数
# #通过闭包生成不同函数
# def hello(msg,count):
# 	result = msg *count
# 	return result
# result = hello("b",10)
# print(result)
#
# def hello(msg,count):
#
# 	def return_msg():
# 		result = msg *count
# 		return result
# 	return return_msg
#
# new_func1 = hello("a",10)
#
# new_func2=hello("b",10)
# #根据不同的参数返回不同的函数
# print(new_func1,new_func2,"---------")
#
# value = new_func1()
# result = new_func2()
# print(value)
# print(result)
#装饰器:一些操作,文件
#装饰器:本质上也是一个函数,可以给原函数的功能进行扩展
#不改变原函数额定义和调用的操作
def show():
	print("AAA")
#在AAA前面加上------(装饰器本质是一个闭包)
# show()
#装饰器函数了
def decorator(new_func):

	#定义
	def inner():
		print("----")
		#调用传进来的函数
		new_func()
	return inner
#相当于重新给show赋值,show就是inner
show = decorator(show)
#相当于调用inner,而不是调用show
show()




