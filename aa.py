import requests
from lxml.html import fromstring, tostring
resp = requests.get('https://catalog.data.gov/dataset')
print(resp.content)


