# -*- coding: utf-8 -*-
import requests
import json
from random import randint
from time import sleep
if __name__ == '__main__':
     unicornHeader = {
        'Referer': 'https://www.ikjzd.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
     }
     # 排名
     i = 1;
     for i in range(1, 384):
         print(i);

         #0102
         sleep(randint(1, 8))
         url = "https://www.ikjzd.com/a/14242.html"
         resp = requests.get(url, headers=unicornHeader, timeout=30)

         sleep(randint(1, 8))
         url = "https://www.ikjzd.com/a/14237.html"
         resp = requests.get(url, headers=unicornHeader, timeout=30)

         sleep(randint(1, 8))
         url = "https://www.ikjzd.com/a/14235.html"
         resp = requests.get(url, headers=unicornHeader, timeout=30)

         sleep(randint(1, 8))
         url = "https://www.ikjzd.com/a/14224.html"
         resp = requests.get(url, headers=unicornHeader, timeout=30)

         #0103
         sleep(randint(1, 8))
         url = "https://www.ikjzd.com/a/14331.html"
         resp = requests.get(url, headers=unicornHeader, timeout=30)

         sleep(randint(1, 8))
         url = "https://www.ikjzd.com/a/14327.html"
         resp = requests.get(url, headers=unicornHeader, timeout=30)


