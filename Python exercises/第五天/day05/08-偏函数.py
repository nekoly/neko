#偏函数:通俗理解就是指函数的参数偏爱某个值,这种函数就叫做偏函数
import functools
def show(num1,num2,num3=3):

	result = num1+num2+num3
	return result

result = show(1,2)
result = show(1,2,4)
print(result)



#定义一个偏函数

def show2(num1,num2,num3=4):
	#在函数内部调用上一个函数
	result = show(num1,num2,num3)
	return result

result=show2(1,2)
print(result)

#偏函数的简写方式(返回的函数就是骗函数)
newfunc = functools.partial(show2,num2=1)
result = newfunc(1)
print(result)
#在内部函数使用偏函数
result = int("123")
print(type(result))
#利用偏函数对系统内置函数设置偏爱值,数据类型转换按照2进制方式转换
newfunc=functools.partial(int,base=2)
result = newfunc("10")
print(result)

