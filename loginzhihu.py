# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 15:54:33 2017

@author: caicai
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 09:18:44 2017

@author: caicai
"""

from selenium import webdriver
import time
import requests
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

cookie= driver.get_cookies()
print(cookie)

driver.close()

[{'expiry': None, 'httpOnly': True, 'secure': False, 'name': 'aliyungf_tc', 'value': 'AQAAAP/mGVo/agIAa9C/d8BlbipKRyj6', 'path': '/', 'domain': 'www.zhihu.com'}, 
 {'expiry': None, 'httpOnly': False, 'secure': False, 'name': 'l_n_c', 'value': '1', 'path': '/', 'domain': '.zhihu.com'}, 
{'expiry': None, 'httpOnly': False, 'secure': False, 'name': 'q_c1', 'value': '94925cacd3224c3c904103d2b8100631|1505207517000|1505207517000', 'path': '/', 'domain': '.zhihu.com'}, 
{'expiry': None, 'httpOnly': False, 'secure': False, 'name': '_xsrf', 'value': '221fa7808498513e1714371f6fcbf29b', 'path': '/', 'domain': 'www.zhihu.com'}, 
{'expiry': None, 'httpOnly': False, 'secure': False, 'name': 'r_cap_id', 'value': '"MWEyZjU1MWQ4ZDA5NDM4Mzg5ODQ4YThjNTkzYzVkZjY=|1505207517|de30a9a0e4e729a40289c5f09483a671cd85049b"', 
'path': '/', 'domain': '.zhihu.com'}, 
{'expiry': None, 'httpOnly': False, 'secure': False, 'name': 'cap_id', 'value': '"ZmE4ODk3ZDkxZDUzNDZjZWI2MmJjYzRiYzY4NGUyMzc=|1505207517|a1866da8fb33da62371f0aecc207bec36e87f959"',
 'path': '/', 'domain': '.zhihu.com'}, 
 {'expiry': None, 'httpOnly': False, 'secure': False, 'name': 'l_cap_id', 'value': '"YjgxNmIzOGFlZDBlNGMwNWJmNTAxNzA1ZmNkYzM5ODQ=|1505207517|afcdbd9580e85a646deb95852880059270ffea38"', 
 'path': '/', 'domain': '.zhihu.com'}, {'expiry': None, 'httpOnly': False, 'secure': False, 'name': 'n_c', 'value': '1', 'path': '/', 'domain': '.zhihu.com'}, 
{'expiry': None, 'httpOnly': False, 'secure': False, 'name': 'd_c0', 'value': '"AGDCmbBqXQyPTpVEKk9LSofVYfYKyDQPN0w=|1505207522"', 'path': '/', 'domain': '.zhihu.com'},
 {'expiry': None, 'httpOnly': False, 'secure': False, 'name': '_zap', 'value': '16c81eb0-9c1a-4a36-97e1-f3f48d9d02fb', 'path': '/', 'domain': '.zhihu.com'}, 
{'expiry': None, 'httpOnly': False, 'secure': False, 'name': '__utma', 'value': '51854390.132757319.1505207526.1505207526.1505207526.1', 'path': '/', 'domain': '.zhihu.com'}, 
{'expiry': None, 'httpOnly': False, 'secure': False, 'name': '__utmb', 'value': '51854390.0.10.1505207526', 'path': '/', 'domain': '.zhihu.com'}, 
{'expiry': None, 'httpOnly': False, 'secure': False, 'name': '__utmc', 'value': '51854390', 'path': '/', 'domain': '.zhihu.com'}, 
{'expiry': None, 'httpOnly': False, 'secure': False, 'name': '__utmz', 'value': '51854390.1505207526.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)', 'path': '/', 'domain': '.zhihu.com'}
, {'expiry': None, 'httpOnly': False, 'secure': False, 'name': '__utmv', 'value': '51854390.000--|3=entry_date=20170912=1', 'path': '/', 'domain': '.zhihu.com'}]

[{'name': 'aliyungf_tc', 'expiry': None, 'domain': 'www.zhihu.com', 'path': '/', 'secure': False, 'httpOnly': True, 'value': 'AQAAABOOoUOv3AYAa9C/d0vSCFphHrXl'},
 {'name': 'l_n_c', 'expiry': None, 'domain': '.zhihu.com', 'path': '/', 'secure': False, 'httpOnly': False, 'value': '1'}, 
{'name': 'q_c1', 'expiry': None, 'domain': '.zhihu.com', 'path': '/', 'secure': False, 'httpOnly': False, 'value': '7e3df7712b65455ea07974e58f6cef57|1505207778000|1505207778000'}, 
{'name': '_xsrf', 'expiry': None, 'domain': 'www.zhihu.com', 'path': '/', 'secure': False, 'httpOnly': False, 'value': '1b800e7fe218c3a53284210f2b1834bc'}, 
{'name': 'r_cap_id', 'expiry': None, 'domain': '.zhihu.com', 'path': '/', 
'secure': False, 'httpOnly': False, 'value': '"YjIzN2Q3ZWVmNjY2NGEwMDgxYmY1ZDExYTIwMTkwZGU=|1505207778|d6f47920efa73240b53b3bc3c60412de3630a5f9"'}, 
{'name': 'cap_id', 'expiry': None, 'domain': '.zhihu.com', 'path': '/', 'secure': False, 'httpOnly': False, 
'value': '"NTIwZDAzYjAwNjhhNDliNGEwNTVjOGY4NzdlNDY0ZjY=|1505207778|b6b57ac97108d1285dac0ddb14b0817d86c2455f"'},
 {'name': 'd_c0', 'expiry': None, 'domain': '.zhihu.com', 'path': '/', 'secure': False, 'httpOnly': False, 'value': '"AFBC865rXQyPTrIy7usB9vllCqBrKy5_PTE=|1505207783"'}, 
{'name': '_zap', 'expiry': None, 'domain': '.zhihu.com', 'path': '/', 'secure': False, 'httpOnly': False, 'value': '27e9e45c-4ec4-48ce-9823-d69b6b941e2b'}, 
{'name': '__utmc', 'expiry': None, 'domain': '.zhihu.com', 'path': '/', 'secure': False, 'httpOnly': False, 'value': '51854390'}, 
{'name': '__utma', 'expiry': None, 'domain': '.zhihu.com', 'path': '/', 'secure': False, 'httpOnly': False, 'value': '51854390.19342454.1505207788.1505207788.1505207788.1'}, 
{'name': '__utmb', 'expiry': None, 'domain': '.zhihu.com', 'path': '/', 'secure': False, 'httpOnly': False, 'value': '51854390.0.10.1505207788'}, 
{'name': '__utmz', 'expiry': None, 'domain': '.zhihu.com', 'path': '/', 'secure': False, 'httpOnly': False, 'value': '51854390.1505207788.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'}, 
{'name': '__utmv', 'expiry': None, 'domain': '.zhihu.com', 'path': '/', 'secure': False, 'httpOnly': False, 'value': '51854390.000--|3=entry_date=20170912=1'}, 
{'name': 'z_c0', 'expiry': None, 'domain': '.zhihu.com', 'path': '/', 'secure': False, 'httpOnly': True, 
'value': 'Mi4xc0taa0FBQUFBQUFBVUVMenJtdGREQmNBQUFCaEFsVk5BVFBmV1FDVVhpN0hCNjVOV3VQR2ZpV0Frd2c0OURDNVFn|1505207809|92f4a0c8c0e1a62cde3a560e261fd54d9ddd1a4b'},
 {'name': '_xsrf', 'expiry': None, 'domain': '.zhihu.com', 'path': '/', 'secure': False, 'httpOnly': False, 'value': '1b800e7fe218c3a53284210f2b1834bc'}]


