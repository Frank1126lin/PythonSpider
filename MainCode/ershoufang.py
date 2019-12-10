#! /usr/bin/env python3
# *_* coding: utf-8 *_*
# @File  : ershoufang.py.py
# @Author: Frank1126lin
# @Date  : 12/4/19

# 爬取链家指定城市所有二手房数据
import time
import threading
from city import get_city, cities
from area import get_city_area
from spider import spider


RANDOM_DELAY = True

def write_to_csv(city, area, random_delay):
    '''

    :param city: 城市名
    :param area: 区域名
    :return: 将爬取的数据写入文件：ershoufang-city-area.csv
    '''
    city_ch = cities[city]
    area_ch = get_city_area(city)[area]
    print('Now writing {0}|{1}'.format(city_ch, area_ch), 'to csv')
    with open('ershoufang-{0}-{1}.csv'.format(city_ch, area_ch), 'w') as csvfile:
        for info in spider(city, area, random_delay):
            print("Now wrting:", '|'.join(info[0:4]))
            csvfile.write('|'.join(info))
            csvfile.write("\n")


def main(city, random_delay):
    """
    主程序
    :return:主程序
    """

    area_list = list(get_city_area(city).keys())
    N = len(area_list)
    print(area_list)
    t_list = []
    # 增加多线程处理，每个区域用一个线程爬取
    for area in area_list:
        t =threading.Thread(target=write_to_csv, args=(city, area, random_delay))
        t_list.append(t)
    for t in t_list:
        t.start()
        # 针对每个城市具体的区域进行分别爬取
    for t in t_list:
        # 阻塞主线程
        t.join()




if __name__ == '__main__':
    stime = time.time()
    city = get_city()
    print("Your choice is:", cities[city])
    main(city, random_delay=RANDOM_DELAY)
    etime = time.time()
    print("总共使用了", (etime-stime)/60,'min')

