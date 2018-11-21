import sys
#递归函数:在函数里面调用函数本身就是递归函数
#特性:1.传递2.回归
#死循环
#递归次数:无限递归:默认最多递归1000次
# def show():
# 	show()
#
#
# show()
#不常用
#阶乘
#5 = 5*4*3*2*1
#5! = 5 *4!
#4! = 4 * 3!
#...
#...
#1! = 1

def calc_num(num):
	#当计算到1的阶乘的时候直接返回1,跳出这个递归(循环)
	if num == 1:
		return 1
	else:
		return num * calc_num(num-1)

result = calc_num(5)
print(result)
#获取默认递归的次数(默认1000)
result = sys.getrecursionlimit()
print(result)
#设置递归的次数(系统提供的)
sys.setrecursionlimit(1200)
result = sys.getrecursionlimit()
print(result)
#调用自定义的函数
result = calc_num(1100)
print(result)
