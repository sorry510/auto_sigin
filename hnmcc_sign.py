# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: hnmcc_sign.py(河南移动签到)
cron: 33 9 * * *
new Env('河南移动签到');
"""

import os
import requests

hnmcc_cookie = os.environ.get("hnmcc_cookie")

url = 'https://h5.ha.chinamobile.com/hnmccClientWap/signNewEdition/signDraw4h.do?r=0.07179090996369186'

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh-Hans;q=0.9",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://h5.ha.chinamobile.com",
    "Content-Length": "46",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    "Referer": "https://h5.ha.chinamobile.com/hnmccClientWap/2021/07/signNew/index.html?channel=channel_WDTB&WT.ac_id=220225_QD_WDTB",
    "Cookie": hnmcc_cookie
}

# channel=channel_WDTB&taskId=&from=&group=false
data = {
    "channel": "channel_WDTB",
    "taskId": "",
    "from": "",
    "group": False
}

res = requests.post(url, headers = headers, data = data).json()
print(res)
