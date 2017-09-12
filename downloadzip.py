# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 11:21:15 2017

@author: caicai
"""

# From 2010 to 2013, the change in median cost of health, dental, and vision coverage for California city employees
from shutil import unpack_archive,get_archive_formats
from statistics import median
import csv
import os
import requests

    
LOCAL_DATADIR = "tmp/capublicpay"
BASE_URL = 'http://publicpay.ca.gov/RawExport/'
##http://publicpay.ca.gov/RawExport/2013_CaliforniaStateUniversity.zip
YEARS = (2010,2013)

medians = []
for year in YEARS:
    basefname = '%s_City.zip' % year
    url = BASE_URL + basefname
    local_zname = "tmp/" + basefname
    # this is such a massive file that we should cache the download
    if not os.path.exists(local_zname):
        print("Downloading", url, 'to', local_zname)
        data = requests.get(url).content
        with open(local_zname, 'wb') as f:
            f.write(data)

    print("Unzipping", local_zname, 'to', LOCAL_DATADIR)

    unpack_archive(local_zname, LOCAL_DATADIR)
    # each zip extracts a file named YEAR_City.csv
    csv_name = LOCAL_DATADIR + '/' + basefname.replace('zip', 'csv')
  
    with open(csv_name, encoding = 'latin-1') as f:
        # first four lines are:
        # Disclaimer
        #
        # The information presented is posted as submitted by the reporting entity. 
    #The State Controller's Office is not responsible for the accuracy of this information.
        cx = list(csv.DictReader(f.readlines()[4:]))
        if year == 2010:
            mx = median([float(row['7136']) for row in cx if row['7136']])
        if year == 2013:
            mx = median([float(row['1370']) for row in cx if row['1370']])
        
        
        print("Median for %s" % year, mx)
        medians.append(mx)

print(medians[-1] - medians[0])