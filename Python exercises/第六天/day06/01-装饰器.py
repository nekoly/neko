#装饰器:本质上就是一个函数,可以给原函数增加新的功能(不改变原函数的情况下)

#装饰器函数(new_func,你给谁增加功能new_func就是谁)
def decorator(new_func):
	#给原本函数增加功能的函数
	def inner():
		print("---")
		#这里才是真正调用show
		new_func()
	#注意返回函数要是函数的名字,如果加括号等于调用函数
	return inner
#相当于修饰了show函数
@decorator#语法糖show = decorator(show)
def show():
	print("BBB")

#调用inner函数
show()

# show = decorator(show)
# show()

