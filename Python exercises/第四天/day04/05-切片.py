#切片:根据下标的方位获取一部分数据:字符串,列表
# my_str = "hello"
# result = my_str[0]
# print(result)
#range()
#起始数据,结束数据(结束数据不),步长
# result = my_str[0:3:1]
# print(result)
# #截取前三个数据(默认步长为0)
# result = my_str[0:3]
# print(result)
# #可以省略前面两个(默认从0开始,取到最后一个)
# result = my_str[::3]
# print(result)
#快速获取整个字符串

# result = my_str[:]
# print(result,"---------")
# #获取最后三个元素
# result = my_str[-3:]
# print(result)
# result = my_str[-2:-5]
# print(result)
#默认的步长是1
#步长是负数才可以反着取
my_str = "hello"
result = my_str[-2:-5]
print(result,"------")
#列表生成式(列表推导式,使用for循环快速创建一个列表)
#引用(内存地址)
#可变类型和不可变类型
#高级函数(返回函数,装饰器)
