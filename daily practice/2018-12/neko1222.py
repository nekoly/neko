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
     for i in range(1,2454):
         print(i);
         # url = "https://www.ikjzd.com/a/12262.html/"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/tl/12328.html/"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/tl/12329.html/"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/tl/12330.html/"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/tl/12331.html/"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/tl/12332.html/"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)

         # url = "https://www.ikjzd.com/tl/12372.html/"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #单品（6000）

         # url = "https://www.ikjzd.com/tl/12371.html/"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/tl/12370.html/"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/tl/12369.html/"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/tl/12368.html/"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/tl/12367.html/"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/a/12502.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/a/12503.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/a/12508.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/a/12509.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/a/12510.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/a/12613.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/a/12627.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/a/12638.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/a/12638.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/a/12652.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/tl/12664.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/tl/12664.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/a/12584.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/a/12708.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/a/12761.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/a/12759.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)

         # url = "https://www.ikjzd.com/a/12828.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #单品（4000）

         # url = "https://www.ikjzd.com/a/12887.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/a/12890.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/a/12893.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/a/12893.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/a/12970.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #
         # url = "https://www.ikjzd.com/a/12975.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)

         # url = "https://www.ikjzd.com/a/13068.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #1214 13068单品（2000）

         # url = "https://www.ikjzd.com/a/13115.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)

         #1217（以下）
         # url = "https://www.ikjzd.com/a/13182.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)

         #1218
         # url = "https://www.ikjzd.com/a/13249.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         # #香熏机
         #
         # url = "https://www.ikjzd.com/a/13256.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)

         # url = "https://www.ikjzd.com/a/13258.htmll"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)

         # url = "https://www.ikjzd.com/a/13339.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)

         # url = "https://www.ikjzd.com/a/13340.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)

         #1220
         # url = "https://www.ikjzd.com/a/13411.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #单5000

         # url = "https://www.ikjzd.com/a/13406.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)
         #3000

         #1221
         # url = "https://www.ikjzd.com/a/13491.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)

         # url = "https://www.ikjzd.com/a/13493.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)

         #1222
         # url = "https://www.ikjzd.com/a/13651.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)

         # url = "https://www.ikjzd.com/a/13648.html"
         # resp = requests.get(url, headers=unicornHeader, timeout=30)

         url = "https://www.ikjzd.com/a/13647.html"
         resp = requests.get(url, headers=unicornHeader, timeout=30)

























