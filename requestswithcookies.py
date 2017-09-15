# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 17:22:14 2017

@author: caicai
"""

import requests
from lxml.html import fromstring
from selenium import webdriver
import time

LOGIN_EMAIL = 'qianzhaicun@163.com'
LOGIN_PASSWORD = 'asdjkl123'
LOGIN_URL = "https://www.zhihu.com/#signin"
login_url2 = 'https://www.zhihu.com/login/email'
def parse_form(html):
    tree = fromstring(html)
    data = {}
    for e in tree.xpath('//form//input'):
        if e.get('name'):
            data[e.get('name')] = e.get('value')
    return data
    
def login(session=None,cookies=None):
    """ Login to example website.
        params:
            session: request lib session object or None
        returns tuple(response, session)
    """
    if session is None:
        html = requests.get(login_url2)
    else:
        html = session.get(login_url2)
    data = {'_xsrf':'d158c8160ea0daf1f574792bd36da0e6','password':'asdjkl123','email':'qianzhaicun@163.com','captcha_type':'cn'}
    if session is None:
        response = requests.post(login_url2, data, cookies=cookies)
    else:
        response = session.post(login_url2, data)
    #print(response.url)
    #assert 'login' not in response.url
    return response, session
    

   

#driver = webdriver.PhantomJS(executable_path='/home/caicai/Downloads/phantomjs-2.1.1-linux-i686 (2)/bin/phantomjs')
chromedriver = "/home/caicai/firefox/geckodriver"
driver = webdriver.Firefox(executable_path=chromedriver)

driver.get('https://www.zhihu.com/#signin')
#js = "https://static.zhihu.com/static/revved/-/js/closure/page-index.db63ea44.js"
#js = requests.get(js)
#js = js.text
#print(js)
#driver.execute_script(js)
time.sleep(2)#signin-switch-password
driver.find_element_by_xpath('//span[@class="signin-switch-password"]').click()
driver.find_element_by_xpath('//input[@name="account"]').clear()
driver.find_element_by_xpath('//input[@name="account"]').send_keys('qianzhaicun@163.com')
driver.find_element_by_xpath('//input[@name="password"]').send_keys('asdjkl123')
time.sleep(15)
driver.find_element_by_xpath('//button[@type="submit"]').click()
time.sleep(5)
title = driver.find_element_by_xpath('//title')
print(title.text)

cookie= driver.get_cookies()[0]


driver.close()
 


session = requests.Session()

response, session = login(session=session,cookies=cookie)
country_html = session.get(LOGIN_URL)
data = {'_xsrf':'d158c8160ea0daf1f574792bd36da0e6','password':'asdjkl123','email':'qianzhaicun@163.com','captcha_type':'cn'}
print(type(cookie))
response = requests.post(login_url2, data, cookies=cookie)
print(response.content)
tree = fromstring(response.content)
print(tree.xpath('//title/text()'))