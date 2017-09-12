from io import BytesIO
from PyPDF2 import PdfFileReader
import requests
import re

from lxml.html import fromstring, tostring

url = 'https://www.fbi.gov/stats-services/publications/bank-crime-statistics-2014/@@castle.cms.querylisting/querylisting-1?'
#pdfbytes = BytesIO(requests.get(url).content)
#pdf = PdfFileReader(pdfbytes)
#txt = pdf.getPage(0).extractText()


response = requests.get(url)
doc = fromstring(response.content)
title = doc.xpath('//div[@class="col-md-9"]//p[@class="title"]/a/text()')
print(title)
# this is really ugly
#                             U.S. DEPARTMENT OF JUSTICE                         FEDERAL BUREAU OF INVESTIGATION                           WASHINGTON, D.C. 20535-0001                           BANK CRIME STATISTICS (BCS)                     FEDERALLY INSURED FINANCIAL INSTITUTIONS                      January 1, 2014 - December 31, 2014  I. VIOLATIONS OF THE FEDERAL BANK ROBBERY AND INCIDENTAL CRIMES STATUTE,                TITLE 18, UNITED STATES CODE, SECTION 2113  Violations by Type of Institution                                Robberies     Burglaries      Larcenies  Commercial Banks                  3,430             61              5 Mutual Savings Banks                31               0              1 Savings and Loan Associations       93               1              0 Credit Unions                      312               8              2 Armored Carrier Companies           13               1              3 Totals:                           3,879             71             11  Grand Total - All Violations:     3,961    Number, Race, and Sex of Perpetrators  The number of persons known to be involved in the 3,961 robberies, burglaries, and larcenies was 4,778.  The following table shows a breakdown of the 4,778 persons by race and sex.  In a small number of cases, the use of full disguise makes determination of race and sex impossible.               White        Black        Hispanic     Other        Unknown              Male         1770         2030         258          68           221 Female       150          160          17           10           12  Unknown Race/Sex: 82  Investigation to date has resulted in the identification of 2,617 (55 percent) of the 4,778 persons known to be involved.  Of these 2,617 identified persons, 1,047 (40 percent) were determined to be users of narcotics, and 463 (18 percent) were found to have been previously convicted in either federal or state court for bank robbery, bank burglary, or bank larceny.  Occurrences by Day of Week and Time of Day  Monday           -      696     6-9 a.m.       -      106 Tuesday          -      669     9-11 a.m.      -    1,037 Wednesday        -      670     11 a.m.-1 p.m. -      929 Thursday         -      648     1-3 p.m.       -      791 Friday           -      803     3-6 p.m.       -      946 Saturday         -      339     6 p.m.-6 a.m.  -      151 Sunday           -       50     Not Determined -        1 Not Determined   -       86  Total:                3,961          Total:         3,961
# relevant line
# Armored Carrier Companies           13               1              3


#https://www.fbi.gov/stats-services/publications/bank-crime-statistics-2014/@@castle.cms.querylisting/querylisting-1?
