#! /usr/bin/env python3
# *_* coding: utf-8 *_*
# @File  : json_to_csv.py
# @Author: Frank1126lin
# @Date  : 12/6/19

import json
import re
with open(r'ershoufang-xiangcheng.json', 'r', encoding="utf-8") as f:
    t = f.read()
    # print(t)

    data = []
    result = re.findall(r'"(.*?)"', t)
    # print(result)
    for i in range(len(result)):
        if i % 2 == 1:
            data.append(result[i])
    # print(data)
# [0:8] [8:16]
    final_data = []
    for i in range(len(data)):
        if i%8 == 0:
            final_data.append(data[i:i+8])
    # print(final_data)
    # for i in final_data:
    #     print("%s-%s-%s-%s-%s-%s-%s-%s"%(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))

    with open(r'ershoufang-xiangcheng2.csv', 'w', encoding="utf-8") as csvf:
        for i in final_data:
            print("%s-%s-%s-%s-%s-%s-%s-%s\n" % (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
            csvf.write("%s|%s|%s|%s|%s|%s|%s|%s\n"%(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))

