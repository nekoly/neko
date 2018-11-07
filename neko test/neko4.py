# -*- coding: utf-8 -*-
import requests
import json
if __name__ == '__main__':
     unicornHeader = {
        'Referer': 'https://www.amazon.co.uk/',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
     }
     # 排名
     rank = 1
     url = "https://junglescoutpro.herokuapp.com/api/v1/sales_estimator?store=uk&rank=" + str(rank) + "&category=Home%20%26%20Kitchen"
     resp = requests.get(url, headers=unicornHeader, timeout=30)
     _json = json.loads(resp.content)
     print('排名第' + str(rank) + '名：月销量:' + str(_json.get('estSalesResult')))

