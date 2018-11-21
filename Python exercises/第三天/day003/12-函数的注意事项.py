#函数的注意事项:1.函数名不能相同
def show():
	print("我好累啊")

def show():
	print("我一点都不累")
#提示一下:如果定义了第二个函数和第一个函数名相同,那么第一个函数不能使用
#覆盖掉了

show()
#定义变量名和函数名相同
#变量名覆盖了函数名,所以不能使用
show = 10

print(show)
show()
#函数里面也可以使用pass
def show():
	pass
def shwo():
	pass

