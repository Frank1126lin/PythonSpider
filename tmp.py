#! /usr/bin/env python3
# *_* coding: utf-8 *_*
# @File  : tmp.py
# @Author: Frank1126lin
# @Date  : 12/5/19

import json

d = {"名称":"我", 2:6, 3:7}
print(d)
print(str(d))
with open("123.txt", "w+") as f:
    f.write(str(d))

with open('123.json', "w") as jsonfile:
    jsondict = json.dumps(d, indent=4, ensure_ascii=False)
    jsonfile.write(jsondict)
    jsonfile.write("\n")