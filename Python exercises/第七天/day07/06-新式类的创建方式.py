#建议大家使用新式类的创建方式
class Teacher(object):
	#类属性
	country = "中国"

	#方法
	def show(self):
		print("哈哈哈")

t1 = Teacher()
print(t1)
