# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 15:01:17 2017

@author: caicai
"""

from login import login, parse_form
import requests
session = requests.Session()
COUNTRY_URL = 'http://example.webscraping.com/places/default/edit/Algeria-4'
response, session = login(session=session)
country_html = session.get(COUNTRY_URL)
data = parse_form(country_html.content)
print(data)
data['population'] = int(data['population']) + 1
response = session.post(COUNTRY_URL, data)
