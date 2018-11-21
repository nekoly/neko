#通用的装饰器,可以修饰任意函数
#定义一个带有参数的函数(2个,3个)

def decorator(func):
	def inner(*args,**kwargs):
		print("计算结果如下",end="")
		result = func(*args,**kwargs)
		return result
	return inner
@decorator
def sum(num1,num2):
	result = num1+num2
	return result
result = sum(1,2)
print(result)

@decorator
def sum1(num1,num2,num3):
	result = num1+num2 +num3
	return result
result = sum1(1,2,4)
print(result)


