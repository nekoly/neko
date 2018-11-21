#__str__:当使用print函数打印对象的时候会调用此方法
class Person(object):

	def __init__(self,name,age):
		#在init方法里面定义的属性就是实例属性
		self.age = age
		self.name = name
	#魔法方法str
	#复写object的方法
	def __str__(self):
		#返回一个字符串信息
		return "我叫:%s 年龄:%d" %(self.name,self.age)

person = Person("张三",18)
print(person)
#访问对象的实例属性
print(person.age)
print(person.name)

