# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 15:11:01 2017

@author: caicai
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 09:18:44 2017

@author: caicai
"""

from selenium import webdriver
driver = webdriver.PhantomJS(executable_path='/home/caicai/Downloads/phantomjs-2.1.1-linux-i686 (2)/bin/phantomjs')
driver.get('http://example.webscraping.com/places/default/search')
driver.save_screenshot('data/python_website.png')
driver.find_element_by_id('search_term').send_keys('.')
js = "document.getElementById('page_size').options[1].text = '1000';"
driver.execute_script(js)
driver.find_element_by_id('search').click()
driver.implicitly_wait(30)
links = driver.find_elements_by_css_selector('#results a')
countries = [link.text for link in links]
print(countries)

driver.close()