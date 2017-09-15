# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 17:07:35 2017

@author: caicai
"""

from rediscache import RedisCache
from threaded_crawler import threaded_crawler
from threaded_crawler import img_callback
from threaded_crawler import main_link_crawler

#import requests
#import urllib.request
#import urllib.parse
#import http.cookiejar
#
#LOGIN_URL = 'http://www.jobbole.com/wp-admin/admin-ajax.php'
#LOGIN_EMAIL = 'caicai'
#LOGIN_PASSWORD = 'asdjkl!@#'
#
#
#postdata = urllib.parse.urlencode({'user_login': LOGIN_EMAIL, 'user_pass': LOGIN_PASSWORD,'action':'user_login'
#    ,'remember_me':'1','redirect_url':'http://www.jobbole.com/'}).encode('utf-8')
#req = urllib.request.Request(LOGIN_URL,postdata)
#req.add_header('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:55.0) Gecko/20100101 Firefox/55.0')
##create CookieJar
#cjar = http.cookiejar.CookieJar()
##create opener
#opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
##open 安装为全局
#urllib.request.install_opener(opener)
#
#file = opener.open(req)
#data=file.read()
#file=open('3.html','wb')
#file.write(data)
#file.close()
#
#url2 = 'http://date.jobbole.com/4510/'
#data2=urllib.request.urlopen(url2).read()
#fhandle=open('4.html','wb')
#fhandle.write(data2)
#fhandle.close()


url = "http://date.jobbole.com/page/0"
##main_pages = main_link_crawler(url, r'^(http://date.jobbole.com/page/)(\d+)/$',max_depth=-1,user_agent="sfdf",robots_url="http://date.jobbole.com/robots.txt")
##print(main_pages)
main_pages = ['http://date.jobbole.com/page/0','http://date.jobbole.com/page/2','http://date.jobbole.com/page/3','http://date.jobbole.com/page/4','http://date.jobbole.com/page/5'
    ,'http://date.jobbole.com/page/6','http://date.jobbole.com/page/7'
    ,'http://date.jobbole.com/page/8','http://date.jobbole.com/page/9','http://date.jobbole.com/page/10','http://date.jobbole.com/page/11'
    ,'http://date.jobbole.com/page/12','http://date.jobbole.com/page/13','http://date.jobbole.com/page/14','http://date.jobbole.com/page/15','http://date.jobbole.com/page/16'
    ,'http://date.jobbole.com/page/17']
if len(main_pages) > 0:
    threaded_crawler(main_pages, r'^(http://date.jobbole.com/)(\d+)/$',max_depth=-1,max_threads=10, img_callback=img_callback,cache=RedisCache(),user_agent="dfdfsfgdf")
        
#import shutil
#import os
#path = '/home/caicai/scrapebole/chp4/data/img/date.jobbole.com'
#dirpath = '/home/caicai/scrapebole/chp4/data/img'
#files = os.listdir(path)
#for file in files:
#    afile = path + '/' + file
#    f = os.listdir(afile)
#    if len(f)==1:
#        ajpg = f[0]
#        os.chdir(afile)
#        shutil.copy(afile + '/'+ ajpg, dirpath)