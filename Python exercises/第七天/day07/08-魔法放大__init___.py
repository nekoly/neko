#魔法方法:当前需要完成某个功能的操作的时候回自行调用的方法

#比如:__init__方法
#魔法方法的表现形式:__开头,__结尾魔法方法
#init,当前对象初始化的时候调用这个方法
class Teacher(object):

	#init方法里面去给对象添加属性
	#创建完成对象后,python自行帮助我们调用的方法
	#self表示当前对象
	def __init__(self,name,age):
		print(name,age)

	def show(self):
		print("这是show方法")

t1 = Teacher("张三",18)
t1.show()

t2 = Teacher("李四",20)
t2.show()
