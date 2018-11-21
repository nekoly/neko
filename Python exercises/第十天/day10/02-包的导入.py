#-----------import导入包里面的模块-----------推荐方式1
# import first_package.first
# # import first_package.second
# # #使用包模块里面的代码
# # first_package.first.show()
# # first_package.second.show_msg()
# #
# # #-----------import 导入设置别名------------
# # import first_package.first as one
# # import first_package.second as two
# # one.show()
# # two.show_msg()
#-----from导入包名 import模块名 推荐方式2
# from first_package import first as one
# from first_package import second
# one.show()
# second.show_msg()

#-----from 包名.模块名 import 功能代码
from first_package.first import show
#需要保证当前模块没有和导入模块的功能代码相同的名字
# def show():
# 	print("这是当前模块")
# show()

#from 包名 import *导入包里面的所有模块
#默认不会导入模块
# from first_package import *
# first.show()
# second.show_msg()
#直接导入包
import first_package
#使用包导入的文件
first_package.first.show()


