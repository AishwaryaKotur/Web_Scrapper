# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 12:02:44 2019

@author: Aishwarya
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

url = input('Enter the url: ')
position = int(input("Enter the position: ")) 
count = int(input("Enter the count: "))

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')

lst = list()
#lst1 = list()

for tag in tags:
        urls = tag.get('href',None)
        #print(urls)
        lst.append(urls)
print(url)
url1 = lst[position-1]
print(url1)
        
for cnt in range(0,count-1,1): 
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    html1 = urllib.request.urlopen(url1, context=ctx).read()
    soup1 = BeautifulSoup(html1, 'html.parser')
    tags1 = soup1('a')
    lst1 = list()
    for tag1 in tags1:
        urls1 = tag1.get('href',None)
        lst1.append(urls1)
    url1 = lst1[position-1]
    print(url1)
