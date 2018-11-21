#1.打开源文件读取数据
src_file = open("2.txt","rb")
#指定写入的路径
dst_file = open("/Users/zhangzhihao/desktop/7.txt","wb")
#一次性读取所有文件里面的所有数据

# file_data =src_file.read(3)
# dst_file.write(file_data)
#python三个方向
#1.pythonweb(制作网页的)豆瓣就业量较少

#2.爬虫 java go python(获取数据)
#找寻数据的客观规律

#3.AI人工智能(机器学习) 数学 物理学 统计学(有基础的同学)
#考研失败,研究生毕业(工科)

#读取
while True:
	file_data =src_file.read(1024)

	#python默认第二次读取就会到上一次读取完毕的地方
	#判断文件是否读取完毕
	#写入数据了
	if file_data>0:
		#执行一次while循环写入1024字节
		dst_file.write(file_data)
	else:
		print("数据读取完成了")
		#没有数据了就不需要读取,也不需要写入
		break

#2.写入读取的数据
src_file.close()
dst_file.close()
