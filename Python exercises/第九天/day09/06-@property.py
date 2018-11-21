class Student(object):

	def __init__(self):
		# 定义了一个私有对象属性
		self.__score = 100
		
	# 将方法修改成对应的属性值
	@property
	def get_score(self):
		# 类的内部可以使用私有属性
		# 返回私有属性
		return self.__score

	@get_score.setter
	def set_score(self, score):
		# 根据你传入的参数
		# 设置私有属性值
		self.__score = score


stu = Student()
# 在外部可以修改私有属性(不建议使用)
# stu.set_score(99)
#
# value = stu.get_score()
# print(value)

stu.set_score = 99

score = stu.get_score

print(score)
