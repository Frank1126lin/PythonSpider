#! /usr/bin/env python3
# *_* coding: utf-8 *_*
# @File  : pg_ana.py
# @Author: Frank1126lin
# @Date  : 2019/12/5

import re
import time
import requests
from headers import create_headers
from city import cities
from area import get_city_area

def pg_ana_re(city, area, pgnum):
    """
    处理单个页面的信息
    return：信息列表
    """
    start_time = time.time()
    data_list = []
    page = 'http://{0}.lianjia.com/ershoufang/{1}/pg{2}'.format(city, area, pgnum)
    print(page)
    headers = create_headers()
    # 获取随机headers
    response = requests.get(page, timeout=10, headers=headers)
    html = response.content.decode('utf-8')
    # print(html)

    # 使用正则表达式解析页面
    pattern  = re.compile(r'<div class="info clear"><div class="title"><a class="" href="(.*?)".*?>(.*?)</a>.*?data-el="region">(.*?)</a>.*?target="_blank">(.*?)</a>.*?<div class="houseInfo"><span .*?></span>(.*?)</div>.*?<div class="totalPrice"><span>(.*?)</span>万</div>.*?单价(.*?)元/平米</span>', re.S)
    data = re.findall(pattern, html)
    # print(data)
    for i in data:
        url = i[0]
        title = i[1]
        xiaoqu = i[2]
        jiedao = i[3]
        miaosu = i [4]
        price = i[5]
        unitprice = i[6]
        format_data = [cities.get(city), get_city_area(city)[area],jiedao, xiaoqu, title, miaosu, price ,unitprice,url ]
        data_list.append(format_data)
    end_time = time.time()
    print('For this page %s, used %s s'%(page, end_time-start_time))
    return data_list

if __name__ == '__main__':
    for i in pg_ana_re("su", "xiangcheng", 1):
        print(i)
