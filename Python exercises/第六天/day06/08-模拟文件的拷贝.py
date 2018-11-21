#1.打开源文件读取数据
import os
#rb比较通用的原因是兼容不同的数据,文本图片视频,都可以
src_file = open("2.txt","rb")
#2.读取(大数据量不行)
file_data =src_file.read()
#打开目标文件,写入数据
#默认写到pychram
#将源数据写入到桌面
dst_file = open("/Users/自己的路径/desktop/haha.txt","wb")
#把源文件内容写到目标文件里面
dst_file.write(file_data)
#关闭文件
dst_file.close()
src_file.close()
#文件夹的操作,模拟大文件的拷贝,面向对象

