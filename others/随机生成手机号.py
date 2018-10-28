#!usr/bin/env python
#-*- coding:utf-8 -*-

'''
@author:mac
@file:随机生成手机号
@time:2018/10/19
'''
#11
# random

'''
电信：133 153，180.。。

联通：130，131，155

移动：134，138，139，

第一位数： 1

第二位数： 3，4，5，7，8

第三位数： 3： 0-9
         4： 5，7，9
         5： 09， ！= 4
         7： 09， ！= 4，9
         8： 0-9

后8位：随机产生
'''

import random
#定义函数
def creat_phone():
	#第一位 1
	
	#第二位数
	second = [3,4,5,7,8][random.randint(0,4)]  #0-4
	
	#根据第二位数获取第三位数
	third = {
		3:random.randint(0,9),
		4:[5,7,9][random.randint(0,2)],
		5:[i for i in range(10) if i != 4][random.randint(0,8)], #[]   range [)
		7:[i for i in range(10) if i not in [4,9]][random.randint(0,7)],
		8:random.randint(0,9)
	}[second]
	
	
	# str_num = ''
	# #获取后八位数d
	# for i in range(8):
	# 	index = random.randint(0,9)
	#
	# 	str_num= str_num+str(index)
	
	ba =  random.randint(10000000,99999999)
	
	
	return "1{}{}{}".format(second,third,ba)

#调用
# num = creat_phone()

num = input("请输入生成的数量：") #10   str

for index in range(0,int(num)):
	
	phone = creat_phone()
	print('第{}个电话号：{}'.format(index+1,phone))
	
