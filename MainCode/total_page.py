#! /usr/bin/env python3
# *_* coding: utf-8 *_*
# @File  : total_page.py
# @Author: Frank1126lin
# @Date  : 12/5/19

import re, time
import requests
from bs4 import BeautifulSoup
from headers import create_headers


def total_page(city, area):
    """
    获取制定城市页面数量
    :param city: 城市代码
    :return: 页面数量int
    """
    start_time = time.time()
    page = 'http://{0}.lianjia.com/ershoufang/{1}'.format(city, area)
    headers = create_headers()
    # 获取随机headers
    response = requests.get(page, timeout=10, headers=headers)
    html = response.content
    soup = BeautifulSoup(html, "lxml")
    # 获得总页数
    try:
        page_box = soup.find_all('div', class_='page-box')[0]
        matches = re.search('.*"totalPage":(\d+),.*', str(page_box))
        total_page = int(matches.group(1))
        end_time = time.time()
        print("total page used:{}s".format(end_time-start_time))
        return total_page
    except Exception as e:
        print("\tWarning: only find one page for {0}".format(city))
        return 1


if __name__ == '__main__':
    print(total_page("su","xiangcheng"))