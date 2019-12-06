#! /usr/bin/env python3
# *_* coding: utf-8 *_*
# @File  : tmp.py
# @Author: Frank1126lin
# @Date  : 12/5/19

import json

# d = {"名称":"我", 2:6, 3:7}
# print(d)
# print(str(d))
fe = ["我","你" ,"她" ]
with open("123.txt", "w") as f:
    f.write('--'.join(fe))

# with open('123.json', "w") as jsonfile:
#     jsondict = json.dump(d, indent=4, ensure_ascii=False)
#     jsonfile.write(jsondict)
#     jsonfile.write("\n")