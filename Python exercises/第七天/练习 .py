# 练习1:
#
# 判断一个路径（目录或文件）是否存在 b = os.path.exists( "你要判断的路径") 若要判断的路径存在，则b的值为 True ,否则b的值为 Flase 。
#
# 请拟定路径如c:\123\456\test.txt样式，并实现判断拟定的路径是否存在的操作：
import os
import os.path
from astropy.wcs.docstrings import name
from boto.gs.lifecycle import AGE
path = 'c:\\123\\456\\test.txt'
fg = os.path.exists(path)
print(fg)

#
# 练习2:
# 判断一个路径是否是文件 b = os.path.isfile( "你要判断的路径")
b = os.path.isfile("c:\\123\\456\\test.txt")
print(b)

# 判断一个路径是否是目录 b = os.path.isdir( "你要判断的路径")
b = os.path.isdir("c:\\123\\456\\")
print(b)


# 根据判断结果正确与否，分别返回True 和 Flase。
#
#
# 练习3:
#
# 定义一个学生类。有下面的类属性：
# 1 姓名
# 2 年龄
# 3 成绩（语文，数学，英语)[每课成绩的类型为整数
#
# 1 获取学生的姓名：get_name() 返回类型:str
# 2 获取学生的年龄：get_age() 返回类型:int
# 3 返回3门科目中最高的分数。get_course() 返回类型:int
# 写好类以后，可以定义2个同学测试下:
# zm = Student('zhangming',20,[69,88,100])
# 返回结果：
# zhangming
# 20
# 100
class Student:
    def __init__(self, name, age, score):
        self.__name = name
        self.__age = age
        self.__score = score
        
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
    
    def get_course(self):
        return max(self.__score)


zm = Student('zhangming', 20, [69, 88, 100])
print(zm.get_name())
print(zm.get_age())
print(zm.get_course())
