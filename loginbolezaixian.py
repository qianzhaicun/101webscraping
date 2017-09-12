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
#driver = webdriver.PhantomJS(executable_path='/home/caicai/Downloads/phantomjs-2.1.1-linux-i686 (2)/bin/phantomjs')
chromedriver = "/home/caicai/firefox/geckodriver"
driver = webdriver.Firefox(executable_path=chromedriver)

driver.get('http://www.jobbole.com/login/?redirect=http%3A%2F%2Fdate.jobbole.com%2F4506%2F')
driver.find_element_by_id('jb_user_login').clear()
driver.find_element_by_id('jb_user_login').send_keys('caicai')
driver.find_element_by_id('jb_user_pass').send_keys('asdjkl!@#')
driver.find_element_by_id('jb_user_login_btn').click()
time.sleep(5)
title = driver.find_element_by_xpath('//title')
print(title.text)

cookie= driver.get_cookies()
print(cookie)

driver.close()