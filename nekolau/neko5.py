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
     for i in range(1, 400):
         print(i);
         # 美国——2018年10月亚马逊美国站户外装饰品类 （Outdoor decor）选品分析报告
         url = "https://www.ikjzd.com/tl/10066.html"
         resp = requests.get(url, headers=unicornHeader, timeout=30)
