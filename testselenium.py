# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 16:36:30 2017

@author: caicai
"""

from selenium import webdriver
#driver = webdriver.Firefox()
chromedriver = "/home/caicai/firefox/geckodriver"
driver = webdriver.Firefox(executable_path=chromedriver)
driver.get('http://example.webscraping.com/places/default/search')
driver.find_element_by_id('search_term').send_keys('.')
js = "document.getElementById('page_size').options[1].text = '1000';"
driver.execute_script(js)
driver.find_element_by_id('search').click()
driver.implicitly_wait(30)
links = driver.find_elements_by_css_selector('#results a')
countries = [link.text for link in links]
print(countries)

driver.close()


#http://example.webscraping.com/places/ajax/search.json?&search_term=a&page_size=10&page=0