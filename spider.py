#! /usr/bin/env python3
# *_* coding: utf-8 *_*
# @File  : spider.py
# @Author: Frank1126lin
# @Date  : 12/5/19



import time
import json
import random
from city import get_city, cities
from area import get_city_area
from pg_ana import pg_ana
from total_page import total_page


def spider(city, area, random_delay=True):
    """
    返回指定城市，指定区域的房产列表信息
    :param city: 指定城市
    :param area: 指定区域
    :return: 房产信息列表，列表格式为[{city:XXX, area:XXX, title:XXX, url:XXX, ...} ]
    """
    # 找出total-page:int
    total_pg = total_page(city, area)
    # 分页爬取每页的数据
    for pgnum in range(1,total_pg+1):
        if random_delay:
            time.sleep(random.randint(0,12))
        print("now crawling:","\n","城市", cities[city],"\n","区域",get_city_area(city)[area])
        print("current page/total page:", pgnum,'/', total_pg)
        for item in pg_ana(city, area, pgnum):
            yield item


if __name__ == '__main__':
    with open('ershoufang-xiangcheng.csv', "w") as infile:
        t1 = time.time()
        count = 0
        for data in spider("su", "xiangcheng", False):
            count+=1
            print("Now writing:", str(data))
            infile.write(str(data))
            infile.write('\n')
        t2 = time.time()
        print("used:",t2-t1,'s, total num:',count)


