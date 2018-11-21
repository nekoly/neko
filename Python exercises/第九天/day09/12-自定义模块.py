#自定义模块:程序员自己创建的模块
#模块的命名规则:和变量命名规则一样
#1.不能以数字开头,可以字母_
#导入模块(将所有的代码赋值过来)
import first_model
import second_model

#可以模块里面的代码
#模块名.变量 模块名.函数名
# print(first_model.g_num)
# first_model.show()
#
# stu = first_model.Student("李四",19)
# stu.show()

result = second_model.sum_num(10,20)
#打印当前模块(主模块)
# print(__name__)

print(result)
