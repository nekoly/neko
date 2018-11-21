#函数嵌套:在函数里面在定义一个函数
def call_able():
	#函数内的函数不能在外部使用
	def text():
		print("我是嵌套函数")
	#返回的是嵌套函数的函数名

	text()
call_able()

a = 10
if a ==10:
	#b全局变量
	b=10

print(b)

