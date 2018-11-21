#约定俗成(类名首字母大写)
#class +类名(继承的父类)
class Teacher(object):
	#方法(谁调用谁就是self)
	def show(self):

		print("今天天气很好")

t1 = Teacher()
#在外部添加属性(动态添加)
t1.name = "李四"
t1.age = "18"

t2 = Teacher()
t2.show()

#获取对象的属性
print(t1.name,t1.age)
t1.show()
