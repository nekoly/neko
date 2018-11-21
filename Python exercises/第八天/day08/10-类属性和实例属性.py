#类属性是在放法和类内部定义的属性
#实例属性:在init方法里面定义的属性
class Person(object):
	#类属性
	type = "黄种人"
	def __init__(self):
		#实例(对象)属性
		self.name = "张三"
		self.age = 29
	#实例方法
	def show(self):
		print("哈哈")

#----------类属性相关的操作----------------
#查看类属性的方法和属性,查看对象方法
print(Person.__dict__)
#访问类属性(使用类名)
print(Person.type)
#修改类属性
Person.type = "白种人"
print(Person.type)
print(Person.__dict__)
#使用类访问对象(实例)属性(不可以使用类名来访问实例属性)
# print(Person.name)

#------------对象属性的操作------------------
person = Person()
#使用对象来访问类属性(可以的)
print(person.type)
#使用对象修改类属性(不可以修改的)
#查看实例属性的函数
print(person.__dict__)
#相当于增加了一个名为type的实例变量
person.type = "黑种人"
print(person.type)
#查看类属性
# print(Person.__dict__)
#查看实例属性的函数
print(person.__dict__)

#总结:类属性由类来完成,
#对象属性由对象来完成,(对象可以访问类属性,但是不可以修改)

#有作业,明天中午之前传,
#授课内容,类方法,静态方法,异常(rasie)