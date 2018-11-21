
#使用了all之后,import *就不是导入所有功能代码了
#指定(限定)功能代码
# __all__ = ["show","g_num"]
#定义一个全局变量
g_num = 10
#定义函数
def show():
	print("我是函数")

class Student(object):
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def show(self):
		print(self.name,self.age)

