g_num = 10


class Student:
	__sex = "男"
	
	@property
	def getSex(self):
		return self.__sex
	
	@getSex.setter
	def setSex(self, sex):
		self.__sex = sex	
		
	def getSex2(self):
		return self.__sex
	
	def setSex2(self, sex):
		self.__sex = sex	

		
def show_info():
	print("show_info")


def sum_num(num1, num2):
	result = num1 + num2
	return result


result = sum_num(1, 2)
print(result)
# print(__name__)
# 判断如果是当前模块再去执行这个代码(是否是主模块)
# if __name__=="__main__":
#
# 	value = sum_num(1,2)
# 	print(value)
