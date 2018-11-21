# 类的三大特性:封装继承多肽
# 继承的好处:子类可以复用父类的属性和方法
class Person(object):
	name = ""
	age = 0

	def __init__(self):
		self.name = "张三"
		self.age = 18

	# 方法
	def show(self):
		print(self.name, self.age)


# 定义一个学生类
class Student(Person):

	def __init__(self):
		self.subject = "数学"


xiao_lan = Student()
# 子类可以调用父类的方法
xiao_lan.show()

print(xiao_lan.age, xiao_lan.name)
