#read()读取全部readline读取一行,readlines
# file = open("1.txt","r")
#
# resulut = file.tell()
# #设置文件的指针为3
# # file.seek(3)
# print(resulut)
# file_data = file.read()
# print(file_data)
# #文件指针
# #设置当前文件的指针
# file.close()

#-----------readline
# file = open("1.txt","rb")
# #只读取一行数据,当遇到\n的时候结束读取
# file_data = file.readline()
#
# print(file_data.decode("utf-8"))
#
# file.close()
#readlines-------------
#文件中的数据按照每行去读取,把每行的数据放到一个列表里面
file = open("1.txt","rb")
file_data = file.readlines()
# content = file_data.decode("utf-8")
# print(content)
for data in file_data:
	print(data.decode("utf-8"),end='')

file.close()