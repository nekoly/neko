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
     for i in range(1, 1593):
         print(i);
         url = "https://www.ikjzd.com/tl/2245.html/"
         resp = requests.get(url, headers=unicornHeader, timeout=30)

         # url = "https://www.ikjzd.com/tl/9116.html/"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/tl/9116.html/"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)

         # url = "https://www.ikjzd.com/tl/11032.html/"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/tl/11036.html/"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/tl/11031.html/"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #


