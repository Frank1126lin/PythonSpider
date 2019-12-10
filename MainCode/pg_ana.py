#! /usr/bin/env python3
# *_* coding: utf-8 *_*
# @File  : pg_ana.py
# @Author: Frank1126lin
# @Date  : 2019/12/5

import re
import time
import requests
from bs4 import BeautifulSoup
from headers import create_headers
from city import cities
from area import get_city_area

def pg_ana(city, area, pgnum):
    """
    处理单个页面的信息
    return：信息列表
    """
    start_time = time.time()
    data_list = []
    page = 'http://{0}.lianjia.com/ershoufang/{1}/pg{2}'.format(city, area, pgnum)
    # print(page)
    headers = create_headers()
    # 获取随机headers
    response = requests.get(page, timeout=10, headers=headers)
    html = response.content
    soup = BeautifulSoup(html, "lxml")
    # 使用bs4解析页面
    house_elements = soup.find_all('li', class_="clear")
    for house_elem in house_elements:
        price = house_elem.find('div', class_="totalPrice")
        unit_price = house_elem.find('div', class_="unitPrice")
        name = house_elem.find('div', class_='title')
        addr = house_elem.find('div', class_='positionInfo')
        # print(addr)
        url = re.search(r'.*?href="(.*?)".*', str(addr))
        # print(url.group(1))
        desc = house_elem.find('div', class_="houseInfo")
        # 查找数据
        price = price.text.strip()
        unit_price = unit_price.text.strip()
        name = name.text.replace("\n", "")
        addr = addr.text.strip().replace(" ","")
        # print(addr)
        url = url.group(1)
        desc = desc.text.replace("\n", "").strip()
        # 清理数据
        # print(price, "\n", name, "\n", desc)
        data=[cities.get(city), get_city_area(city)[area], addr,name, price, unit_price, desc, url]
        data_list.append(data)
    end_time = time.time()
    print("For this page %s , used %s s"%(page, end_time-start_time))
    return data_list

if __name__ == '__main__':
    for i in pg_ana("su", "xiangcheng", 1):
        print(i)
