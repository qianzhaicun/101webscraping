# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 16:04:56 2017

@author: caicai
"""

# The title of the highest paid California city government position in 2010
# note, the code below makes it easy to extend "years" to include multiple years
import csv
import os.path
import requests
from shutil import unpack_archive
LOCAL_DATADIR = "tmp/capublicpay"
YEARS = (2010,) # i.e. just 2010
def foosalary(row):
    return float(row['Total Wages']) if row['Total Wages'] else 0

for year in YEARS:
    bfname = '%s_City' % year
    url = 'http://publicpay.ca.gov/RawExport/%s.zip' % bfname
    zname = os.path.join("tmp", bfname + '.zip')
    cname = os.path.join(LOCAL_DATADIR, bfname + '.csv')

    if not os.path.exists(zname):
        print("Downloading", url, 'to', zname)
        data = requests.get(url).content
        with open(zname, 'wb') as f:
            f.write(data)
    # done downloading, now unzip files
    #print("Unzipping", zname, 'to', LOCAL_DATADIR)
    #unpack_archive(zname, LOCAL_DATADIR, format = 'zip')

    with open(cname, encoding = 'latin-1') as f:
        # first four lines are:
        # Disclaimer
        #
        # The information presented is posted as submitted by the reporting entity. The State Controller's Office is not responsible for the accuracy of this information.
#        data = list(csv.DictReader(f.readlines()[4:]))
#        topitem = max(data, key = foosalary)
#        print(topitem['Entity Name'], topitem['Department / Subdivision'],
#            topitem['Position'], topitem['Total Wages'])
#            
        maxwage = []
        name = ''
        sub = ''
        pos = ''
        reader = csv.reader(f)
        for row in reader:
            awage = row[16]
            if awage.isdigit():
                maxwage.append(int(row[16])) 
        amax = max(maxwage)
        
    with open(cname, encoding = 'latin-1') as f:    
        reader = csv.reader(f)
        for row in reader:
            awage = row[16]
            if awage.isdigit():
                if int(row[16]) == amax:
                    name = row[3]
                    sub = row[4]
                    pos = row[5]
        print(name,sub,pos,amax)
        
