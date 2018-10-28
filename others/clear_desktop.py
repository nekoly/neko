#!usr/bin/env python
#-*- coding:utf-8 -*-

'''
@author:mac
@file:clear_desktop
@time:2018/10/19
'''
import os
import shutil
#桌面的路径

# print()
desktop = os.path.join(os.path.expanduser('~'),'Desktop')
# print(desktop)

name = input('输入整理后的文件夹的名字：')

clean = os.path.join(desktop,name)

#判断是否存在true  false
idExists = os.path.exists(clean)

if idExists == False:
	# 创建文件夹
	os.mkdir(clean)
else:
	pass
	#创建文件夹
	
	
#获取文件
name_list = os.listdir(desktop)

#分类
for file in name_list:
	
	filePath = os.path.join(desktop,file)
	
	if not os.path.isfile(filePath):
		continue
	elif os.path.isfile(filePath):
		
		#分割文件名和扩展名
		fileExpand = os.path.splitext(file)[1]    #.MP4
		
		fileExpand = fileExpand[1:]   #mp4
		# print(fileExpand)
		
		#clean 创建文件夹
		expand_file_name = os.path.join(clean,fileExpand)
		
		if not os.path.exists(expand_file_name):
			os.mkdir(expand_file_name)
		
		#复制到指定路径下
		shutil.move(filePath,expand_file_name)


