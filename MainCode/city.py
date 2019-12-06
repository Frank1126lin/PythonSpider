#! /usr/bin/env python3
# *_* coding: utf-8 *_*
# @File  : city.py
# @Author: Frank1126lin
# @Date  : 12/4/19


cities = {
    'bj': '北京',
    'cd': '成都',
    'cq': '重庆',
    'cs': '长沙',
    'dg': '东莞',
    'dl': '大连',
    'fs': '佛山',
    'gz': '广州',
    'hz': '杭州',
    'hf': '合肥',
    'jn': '济南',
    'nj': '南京',
    'qd': '青岛',
    'sh': '上海',
    'sz': '深圳',
    'su': '苏州',
    'sy': '沈阳',
    'tj': '天津',
    'wh': '武汉',
    'xm': '厦门',
    'yt': '烟台',
}

def choose_city():
    """
    :return:拼接好的字符串
    """
    city_info = []
    count = 0
    for en_name, ch_name in cities.items():
        count+=1
        city_info.append(str(en_name+":"+ch_name))
        if count % 4 ==0:
            city_info.append("\n")
    return "".join(city_info)+"\n"+"Which city do you want to choose?\n"

# print(choose_city())

def get_city():
    """
    支持函数调用，并返回城市英文代码
    :return: en_name
    """
    city_name = input(choose_city())
    if len(city_name) == 2:
        if cities.get(city_name):
            return city_name
        else:
            print("No such city!")
    else:
        print("only accept 2 words.")

if __name__ == '__main__':
    pass