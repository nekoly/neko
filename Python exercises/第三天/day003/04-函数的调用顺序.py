#定义函数是不会执行函数体里面的代码
def shwo():
	print("哈哈")

print("呵呵")

shwo()
print("lll")
#总结:函数调用的时候会返回到函数的定义处,执行函数体里面的代码
#执行完毕,返回的调用处