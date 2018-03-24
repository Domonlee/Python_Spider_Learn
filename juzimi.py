#!/usr/bin/python
# -*- coding: utf-8 -*-
# 获取经典句子

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0',}

def get_html(url):
    r = requests.get(url,headers = headers)
    html = r.content
    return html

def get_juzi(html):
    soup = BeautifulSoup(html,"lxml")
    juziList = soup.find_all('a',class_="xlistju")
    for x in juziList:
        print x.get_text().encode('utf-8')
        print

def get_title(html):
    soup = BeautifulSoup(html,"lxml")
    print soup.title.get_text().encode('utf-8').replace('句子迷','')

if __name__ == '__main__':
    for item in range(8):
        url = 'http://www.juzimi.com/article/316132?page=%s' % item
        html = get_html(url)
        if item == 0:
            get_title(html)
        get_juzi(html)
