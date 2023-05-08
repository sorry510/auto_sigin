# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: hnmcc_sign.py(yd66微信签到)
cron: 33 9 * * *
new Env('yd66微信签到');
"""

import os
import requests

yd66_query = os.environ.get("yd66_query")

url = 'https://zxkwx-boot.hacitd.com/wx-act/signAct/signActApi/signInNow/?' + yd66_query

headers = {
    "Accept": "*/*",
    "X-Requested-With": "XMLHttpRequest",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh-Hans;q=0.9",
    "Connection": "keep-alive",
}

res = requests.get(url, headers = headers).json()
print(res)
