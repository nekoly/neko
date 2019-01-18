# -*- coding: utf-8 -*-
import requests
import json
from random import randint
from time import sleep
if __name__ == '__main__':
     # 排名
     i = 1;
     
     unicornHeader = {
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "accept-encoding":"gzip, deflate, br",
            "accept-language":"zh-CN,zh;q=0.9",
            "cache-control":"no-cache",
            "pragma":"no-cache",
            "upgrade-insecure-requests":"1",
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
     }
      
     for i in range(1, 1951):
         print(i);
         # url = "https://www.ikjzd.com/a/12262.html/"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)

        
         # sleep(randint(1, 3))
         # url = "https://www.ikjzd.com/index/ArticleApi/PViews?id=14594"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         # print(resp.text)

         sleep(randint(1, 10))
         url = "https://www.ikjzd.com/index/ArticleApi/PViews?id=15389"
         resp = requests.get(url, headers=unicornHeader, timeout=30)
         print(resp.text)
        
         # url = "https://www.ikjzd.com/a/14594.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         # print(resp.text)


        
        # print(unicornHeader)
        # url = "https://www.ikjzd.com/index/Note/getComment/page/1"
        # _data = {"id":14713, "replyid":1}
        # resp = requests.post(url, headers=unicornHeader, data=_data, timeout=30)
        # print(resp.text)
