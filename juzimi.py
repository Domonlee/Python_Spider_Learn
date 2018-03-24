#!/usr/bin/python
# -*- coding: utf-8 -*-
# 获取经典句子

import requests
from bs4 import BeautifulSoup
import connector
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0', }
content = []
title = []


def get_html(url):
    r = requests.get(url, headers=headers)
    html = r.content
    return html


def get_juzi(html):
    soup = BeautifulSoup(html, "lxml")
    juziList = soup.find_all('a', class_="xlistju")
    for x in juziList:
        content.append(x.get_text().encode('utf-8'))


def get_title(html):
    soup = BeautifulSoup(html, "lxml")
    print soup.title.get_text().encode('utf-8').replace('句子迷', '')


def get_main_title(html):
    soup = BeautifulSoup(html, "lxml")
    titleList = soup.find_all('a', class_="xqallarticletilelink")
    for x in titleList:
        title.append(x.get_text().encode('utf-8'))


if __name__ == '__main__':
    l = []
    baseUrl = 'http://www.juzimi.com/'

    mainUrl = baseUrl + 'allarticle/jingdiantaici?page='
    innerUrl = baseUrl + 'article/316132?page='

    for item in range(2):
        url = mainUrl + '%s' % item
        html = get_html(url)
        # if item == 0:
        #     get_title(html)
        # get_juzi(html)
        # l.append(content)

        get_main_title(html)

    # print json.dumps(title, encoding='utf-8', ensure_ascii=False)
    print str(title).decode('string_escape')

    # connector.insert_list(content)
