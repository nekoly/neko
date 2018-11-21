# def decorator(func):
# 	def inner():
# 		print("AAA")
# 		func()
# 	return inner
#
# def decorator1(func):
# 	def inner():
# 		print("BBB")
# 		func()
# 	return inner

# @decorator1("bbb")
#定义一个带有参数的装饰器函数
#get函数的目的就是返回一个装饰器函数
def get_decorator(char):

	def decorator(func):
		def inner():
			print(char)
			func()
		return inner
	return decorator

#@符号后面是装饰器函数
@get_decorator("aaa")
def show():
	print("11111")

show()
