# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 17:22:14 2017

@author: caicai
"""

import requests
from lxml.html import fromstring
f = open('cookies')
cookies2 = f.read()
f.close()
url = "https://www.zhihu.com/#signin"
r = requests.get(url)
print(r.content)
tree = fromstring(r.content)
print(tree.xpath('//title/text()'))