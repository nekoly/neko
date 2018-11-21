
def show_msg(**kwargs):
	print(kwargs)


#定义不定长关键字函数
def show(**kwargs):
	print(kwargs)
	#使用了位置传参的方式调用函数
	# show_msg(a=kwargs)
	# 对字典进行拆包
	show_msg(**kwargs)


show(a=1,b=2)
