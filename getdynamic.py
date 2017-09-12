# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 10:15:41 2017

@author: caicai
"""

##http://example.webscraping.com/places/ajax/search.json?&search_term=.&page_size=10&page=0
import requests
import string
import random
import time
PAGE_SIZE = 1000
pro = ['1.119.129.2:8080','115.174.66.148', '113.200.214.164']
template_url = 'http://example.webscraping.com/places/ajax/' + 'search.json?page={}&page_size={}&search_term={}'
countries = set()
letter = '.'  
if letter == '.':
#for letter in string.ascii_lowercase:
    letter = '.'    
    print('Searching with %s' % letter)
    page = 0
    while True:
        headers = {'user-agent': 'Mozilla/5.0 (X11; Linux i686; rv:55.0) Gecko/20100101 Firefox/55.0'}
        ##proxies={'http': random.choice(pro)}
        #time.sleep(3)
        resp = requests.get(template_url.format(page, PAGE_SIZE, letter),headers=headers)
        print(resp.status_code)
        data = resp.json()
        print('adding %d more records from page %d' % (len(data.get('records')), page))
        for record in data.get('records'):
            countries.add(record['country'])
        page += 1
        if page >= data['num_pages']:
            break
        
with open('data/countries.txt', 'w') as countries_file:
    countries_file.write('\n'.join(sorted(countries)))