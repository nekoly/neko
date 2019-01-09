# -*- coding: utf-8 -*-

import requests

test=requests.get('https://www.ikjzd.com/m/12.html/')
print(test.content)



