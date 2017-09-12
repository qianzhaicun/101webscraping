# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 09:18:44 2017

@author: caicai
"""

from selenium import webdriver
#driver = webdriver.PhantomJS(executable_path='/home/caicai/Downloads/phantomjs-2.1.1-linux-i686 (2)/bin/phantomjs')
chromedriver = "/home/caicai/firefox/geckodriver"
driver = webdriver.Firefox(executable_path=chromedriver)

driver.get('http://example.webscraping.com/places/default/user/login?_next=/places/default/search')
driver.find_element_by_id('auth_user_email').send_keys('example@webscraping.com')
driver.find_element_by_id('auth_user_password').send_keys('example')
driver.find_element_by_xpath('//input[@type="submit"]').click()
driver.implicitly_wait(3)
title = driver.find_element_by_xpath('//h1')
print(title.text)

driver.close()