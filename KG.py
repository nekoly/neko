#!usr/bin/env python
#-*- coding:utf-8 -*-

'''
@author:mac
@file:KG
@time:2018/10/22
'''

'''
1.歌曲的名字
2.搜索，URL?   &。。。。
3.MP4  url?
4.存储到本地

搜索的链接
http://songsearch.kugou.com/song_search_v2?keyword={需要我们传的参数（歌曲的名字)）}&page=1&pagesize=30

这个链接的响应里含有  MP3的链接   1FA2B38DD12A487AB621BC666DE4965E
http://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash={}

下载MP3链接：  从上一个链接中获取
'''
import requests
import json
import re
import os

#类
class Downloader():
	
	def __init__(self,keyword):
		self.keyword = keyword
		self.search_url = 'http://songsearch.kugou.com/song_search_v2?keyword={}&page=1&pagesize=30'
		self.hash_url = 'http://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash={}'
		
		self.headers ={
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
		}
		
		
	def run(self,keyword,num=1):
		
		#搜索歌曲
		res = requests.get(url=self.search_url.format(keyword),headers=self.headers)
		
		# print(res.text)
		#判断是否越界
		dic = json.loads(res.text)
		
		songlist = dic['data']['lists']   #30   50   30
		if num > len(songlist):
			print('歌曲数量一共是%d'%len(songlist))
			num = len(songlist)
		
		#获取hash
		filehash = re.findall('"FileHash":"(.*?)"',res.text) # list
		# print(filehash)
		
		songname = re.findall('"SongName":"(.*?)"',res.text)
		# print(songname)
		
		#保存的路径
		if not os.path.exists('./results'):
			os.mkdir('./results')
		
		names = []
		#歌曲文件的名字  爱你.mp3
		for n in range(num):  #0-1
			#<em>爱你</em>   爱你.mp3
			name = songname[n].replace("<\\/em>","").replace("<em>","") + '.mp3'
		
			if name in names:
				name = str(n)+name
				names.append(name)
			
			content = requests.get(self.hash_url.format(filehash[n]))
			#['http://fs.w.kugou.com\\/201810222154\\/191e76942abc3f54af09db766dbbe903\\/G005\\/M05\\/05\\/09\\/RQ0DAFS4AeCADktlADXYWlohENY063.mp3
			url = re.findall('"play_url":"(.*?)"',content.text)[0]
			
			#链接中\\ 替换
			download_url = url.replace("\\","")
			
			# print(url)
			
			#写入文件
			with open('./results/{}'.format(name),'wb') as f:
				f.write(requests.get(download_url).content)
			
			
while True:

	keyword = input('请输入歌曲名字：')
	songnum = input('输入下载的数量：') #string   type(songnum)  12   ab
	
	try:
		songnum = int(songnum)
	except:
		print('输出信息有误 ')
	
	#创建对象
	loader = Downloader(keyword)
	
	#对象调用方法
	loader.run(keyword,songnum)






