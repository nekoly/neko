#生成器:是一个特殊的迭代器,他同样可以通过next函数和for循环取值

#列表生成式
# result = [x for x in range(4)]
# print(result)
#生成一个生成器
result = (x for x in range(4))
# print(result,type(result))
#测试一下:是next获取下一个值
# value = next(result)
# print(value)
# value = next(result)
# print(value)
# value = next(result)
# print(value)
# value = next(result)
# print(value)
# value = next(result)
# print(value)
#for循环遍历生成器,自动停止迭代
# for value in result:
# 	print(value)

#2.使用yield创建生成器
def show_num():
	for i in range(5):
		#yield 代码遇到它会暂停,然后把结果返回过去
		#下次启动的时候,生成器会在暂停的位置
		#yield 特点:可以返回多次值,return只能返回一次
		yield i

g = show_num()

value = next(g)
print(value)
value = next(g)
print(value)
value = next(g)
print(value)
value = next(g)
print(value)
value = next(g)
print(value)
value = next(g)
print(value)
#生成器也是迭代器,可以直接遍历(用的很少)
# for value in g:
# 	print(value)
