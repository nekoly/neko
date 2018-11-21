# 私有属性:在属性名前面加上__,那么定义的属性就是私有属性
# 私有属性:在方法名前面加上__,那么定义的方法就是私有方法


class Person(object):

	# 爬虫:反扒
	def __init__(self, name, age):
		# 公有属性
		self.name = name
		# 私有属性
		# 注意点:外部访问不了的属性,就叫做私有属性
		# 私有对象属性都是在init方法里面添加的
		self.__age__ = age

	# 公有方法
	def show(self):
		print("公有方法")

	# 私有方法
	def __money(self):
		print("100万")


# 创建对象
person = Person("zhangsan", 10)
# 访问私有属性
print(person.name)
# 报错
# print(person.__age)
# 这里不是修改私有属性,给person对象动态添加了一个公有属性
# person.__age = 20
# # print(person.__age)
# # #查看对象中的属性信息(公有私有都会打印)
print(person.__dict__)
#
# #调用方法------------------------
# person.show()
# #不可以调用私有方法
# # person.__money()
# #打印所有的方法(注意点,用类名调用)
print(Person.__dict__)
#
# #不建议使用(非常规操作)
# # #注意点:在python中,没有真正的私有方法,和私有函数(伪装的)
# #设置私有属性值
person._Person__age = 30
print(person.__dict__)
# #查看私有属性
print(person._Person__age)
# #调用私有方法
person._Person__money()
