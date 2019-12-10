#! /usr/bin/env python3
# *_* coding: utf-8 *_*
# @File  : ershoufang.py.py
# @Author: Frank1126lin
# @Date  : 12/4/19

# 爬取链家指定城市所有二手房数据
import time
from city import get_city, cities
from area import get_city_area
from WebSpider.spider import spider

def main():
    """
    主程序
    :return:返回列表嵌套结果,写入文件
    """
    city = get_city()
    print("Your choice is:", cities[city])
    with open('ershoufang-{0}.csv'.format(city), 'w') as csvfile:
        for area in get_city_area(city).keys():
            # 针对每个城市具体的区域进行分别爬取
            print("当前爬取",cities[city], get_city_area(city)[area])
            for info in spider(city, area):
                print("Now writing:", info)
                csvfile.write('--'.join(info))
                csvfile.write("\n")



if __name__ == '__main__':
    stime = time.time()
    main()
    etime = time.time()
    print("Used:", etime-stime)

