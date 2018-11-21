#无参数无返回值得函数
def show():
	#函数'体里面的代码执行完毕,返回到函数的调用出
	print("大家好,今天天气可冷了")

#函数调用
show()

#无参数有返回值的函数
def show():
	result = 10
	#带着数据返回到代码的调用处
	return result

value = show()
print(value)
#有参数无返回值的
def show(name,age):
	print("我叫:%s 年龄:%d" %(name,age))
show("张三",19)

#有参数有返回值的
def show_msg(name,age):
	msg = "我叫:%s 年龄:%d" %(name,age)
	return msg

result = show_msg("李四",40)
print(result)
