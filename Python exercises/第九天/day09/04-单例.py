#单例:设计模式 常用设计模式
#在应用内,不管创建多少次对象,都是同一个对象
class Person(object):

	#私有属性
	__instance = None
	def __new__(cls, *args, **kwargs):

		#第一创建对象
		if cls.__instance ==None:
			#创建对象
			print("创建对象和")
			#把创建的对象赋值给类属性
			#object.__new__(cls)创建对象
			cls.__instance =object.__new__(cls)
		#第一次返回的是创建的对象
		#第二次不满足if判断语句,直接返回雷属性(赋值为对象的类属性)
		return cls.__instance

	def __init__(self,name,age):
		self.name = name
		self.age = age
		print("初始化")
	#不同对象调用show方法会有不同的实现
	#相同的对象调用show方法会有相同的实现
	#数据库(对象去访问数据库)
	def show(self):
		print("这是show方法")

#多线程 协成 进程
#p1引用计数是多少
p1 = Person("zhangsan",18)
#覆盖掉了,重新赋值
p2 = Person("李四",19)
print(p1.name)
print(p1,p2)



# p2 = Person()
#
# p3 = Person()
#
# print(p1)
# print(p2)
# print(p3)


#10数据库1-100 (1-10)(10-20)
#取出数据库的数据
#创建数据库对象取数据






