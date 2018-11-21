
#定义不定长位置参数
def show_msg(*args):
	#(1,2)
	print(args)

#定义不定长位置参数

def show(*args):
	# print(args,type(args))
	# (1,2)
	print(args)
	#解决办法:对元组进行拆包
	show_msg(*args)

	# show_msg(args)

show(1,2)