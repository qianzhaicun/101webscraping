# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 14:14:11 2017

@author: caicai
"""

from urllib.parse import urlencode
from urllib.request import Request, urlopen
from lxml.html import fromstring
import requests
def parse_form(html):
    tree = fromstring(html)
    data = {}
    for e in tree.cssselect('form input'):
        if e.get('name'):
            data[e.get('name')] = e.get('value')
    return data

LOGIN_URL = 'http://example.webscraping.com/places/default/user/login'
LOGIN_EMAIL = 'example@webscraping.com'
LOGIN_PASSWORD = 'example'

html = requests.get(LOGIN_URL)
data = parse_form(html.content)
data['email'] = LOGIN_EMAIL
data['password'] = LOGIN_PASSWORD
response = requests.post(LOGIN_URL, data)
print(data)
print(response.url)

second_response = requests.post(LOGIN_URL, data, cookies=html.cookies)
print(second_response.url)