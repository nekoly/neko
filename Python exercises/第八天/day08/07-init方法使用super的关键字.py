
#类的名字命名规则见名知意
class AA(object):
	#复写父类的方法
	def __init__(self,name):
		print("A")
		self.name = name
#父类不可以使用子类里面的方法和属性
class B(AA):
	#提示一下:如果子类复写了父类的方法,那么不会执行父类的方法
	def __init__(self):
		#调用父类的init方法(调用本身类的方法)
		# self.__init__("张三")
		#使用类名(注意点必须传入对象)
		# AA.__init__(self,"张三")
		# print("BB")
		#类继承链的方法
		#super()._ 相当于super(B,self)
		#如果不传参数,代用当前类的下一个类,当前链条
		self.subject = "数学"
		super().__init__("王五")
		print(self.__class__.mro())


b = B()
print(b.name)
