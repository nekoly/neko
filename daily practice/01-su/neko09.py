# -*- coding: utf-8 -*-
import requests
import json
if __name__ == '__main__':
     unicornHeader = {
        'Referer': 'https://www.ikjzd.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
     }
     # 排名
     i = 1;
     for i in range(1,1951):
         print(i);
         # url = "https://www.ikjzd.com/a/12262.html/"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)

         sleep(randint(1, 3))
         url = "https://www.ikjzd.com/a/14018.html"
         resp = requests.get(url, headers=unicornHeader, timeout=30)