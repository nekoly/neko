#序列化:把内存的数据保存到本地,可以做到数据持久化
import pickle #通用,可以序列化任何数据
#
# my_list = [{"name":"李四","age":"20"},{"name":"王五","age":"19"}]
# # #得到的数据是二进制数据,想要写入文件,文件的访问模式是"wb"
# file = open("mylist.serialize","wb")
# pickle._dump(my_list,file)
# file.close()
# #
# #反序列化,:把文件中的数据读取出来,获得一个python对象
# file = open("mylist.serialize","rb")
# #反序列化的操作
# my_list = pickle.load(file)
# print(my_list)
# file.close()
#序列化类
class Student(object):
	def __init__(self):
		self.name = "张三"
		self.age = 10

stu = Student()
file = open("stu.txt","wb")
#序列化自定义类型的对象(序列化对象,本质上就是序列化对象里面的属性)
pickle._dump(stu,file)
file.close()

# 反序列化
file = open("stu.txt","rb")
stu = pickle.load(file)
print(stu.name,stu.age)
file.close()