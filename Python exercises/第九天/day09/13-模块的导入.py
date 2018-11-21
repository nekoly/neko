#_____________import导入模块__________-常用方式
# import first_model
#
# stu = first_model.Student("张三",18)
# print(stu.name,stu.age)
# print(first_model.g_num)

#--------------from模块名 import 功能代码 导入模块_____
#常用方式
#
#_________from模块名 import *(导入所有模块的功能)----
#__all__限定导入功能代码
# from first_model import *
# print(g_num)
# show()
# Student()
#给 import 模块名 设置别名
# import first_model as first
#
# print(first.g_num)
#from 模块名 import 功能代码设置别名

from first_model import show as show_msg
from first_model import Student as Stu
show_msg()
s1 = Stu("lisi",18)
s1.show()
