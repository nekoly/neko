#_*_ coding:utf-8 _*_
#python2默认不支持中文
#类的定义,使用class关键字 创建的(特征和行为)
#类有属性(特征)和方法(行为)
#定义老师类
#旧式类的创建方式
#创建一个Teacher的类继承object
#在python2中如果不写object那么没有父类
class Teacher():
	#属性(国籍)
	country = "中国"
	#方法
	def show(self):
		print("我是大家今天的授课老师")
#类图纸,对象是根据图纸绘制出来的
#通过类创建对象(在内存中开辟了一块空间,空间存的是对象的内存地址)
teacher = Teacher()
teacher1 = Teacher()
#通过对象查看属性
print(teacher.country)
#通过对象调用方法
teacher.show()

print(teacher)
print(teacher1)
#查看父类(不继承object)会少了很多父类提供的方法
print(Teacher.__bases__)
#根据现实生活中抽拟出一个类,写上对象的属性和方法
