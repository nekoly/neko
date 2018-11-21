#定义一个装饰器
def decorator(func):

	def inner(num1,num2):
		print("计算结果如下:")
		#调用的时候要知道真正调用的是哪个函数
		#func才是真正的sum
		result = func(num1,num2)
		#返回结果
		return result

	return inner



#定义了一个带有参数的函数,装饰器修饰他
@decorator
def sum(num1,num2):

	result =num1+num2

	return result

result = sum(2,3)

print(result)
