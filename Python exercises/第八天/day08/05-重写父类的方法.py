#重写:子类继承父类,父类的方法满足不了子类
#可以对父类的方法进行重写
class Person(object):
	def run(self):
		print("跑起来")

class Student(Person):
	def __init__(self,name,age):
		self.name = name
		self.age = age
	#子类重写父类的方法, 因为满足不了子类的需求
	def run(self):

		print("%s跑起来了" %self.name)

stu = Student("张三",18)
stu.run()
#总结:调用方法的时候,先去本类找,如果本类没有找到的话,去父类找
#父类没有找到,去爷爷类--->object
#尊徐mro的特点
print(Student.mro())
