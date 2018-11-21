# 练习1:
# 请编写一段符合多态特性的代码.
class A:

    def call(self):
        print("A")

    
class B(A):

    def call(self):
        print("B")


# 显示数据的方法
def show_data(data):
    data.call()

     
b = B()
show_data(b)

a = A()
show_data(a)


# 练习2:下面三种实现单例的方法,哪一种写法是正确的,
class Single(object):
    __instance = None

    def __new__(cls):
        if not cls.__instance:
        	# 写法一
            # cls.__instance = Single() #

            # 写法二
            # cls.__instance = super(Single, cls).__new__(cls)

            # 写法三
            cls.__instance = object.__new__(cls)

        return cls.__instance


A = Single()
B = Single()
print(id(A))
print(id(B))
# 练习3.创建自定义模块second_module
# second_module模块定义了全局变量,类(属性为私有,固定为(sex="男")),函数
# (1)列举不同导入的方式(注释说明不同)
# 导入所有模块和方法


from day09.second_model import *

# 指定方法 重命名别名
from day09.second_model import Student as Stu

# 指定方法
from day09.second_model import Student

# (2)#在主模块中只想使用second_module中的类,其他不使用如何导入
from day09.second_model import Student

# (3)在主模块利用second_module模块中的类创建对象,
from day09.second_model import Student
student = Student()

# 创建对象之后:将私有属性修改为("女")(利用两种方式修改)
student.setSex = "女"
print(student.setSex)

student.setSex2("女")
print(student.getSex2())
