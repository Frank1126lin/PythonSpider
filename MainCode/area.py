#! /usr/bin/env python3
# *_* coding: utf-8 *_*
# @File  : area.py.py
# @Author: Frank1126lin
# @Date  : 12/5/19

import requests
import re
from bs4 import BeautifulSoup
from headers import create_headers
from city import cities


def get_city_area(city):
    """
    返回指定城市的的区域信息
    :param city: 城市代码
    :return: 区域列表中英文字典exam:gongyeyuan:工业园区
    """
    page = 'http://{0}.lianjia.com/ershoufang/'.format(city)
    headers = create_headers()
    # 获取随机headers
    data_dic={}
    response = requests.get(page, timeout=10, headers=headers)
    html = response.content
    soup = BeautifulSoup(html, "lxml")
    area_elements = str(soup.find_all('div', class_="position"))
    # print(area_elements)
    area_list = re.findall(r'.*?/ershoufang/(.*?)/.*?title="{0}(.*?)在售.*?'.format(cities[city]), area_elements)
    for tup in area_list:
        data_dic[tup[0]]=tup[1]
    # print(data_dic)
    return data_dic



if __name__ == '__main__':
    print(get_city_area('sh'))