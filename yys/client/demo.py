#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import traceback
import requests
import time
import json

base_url = 'https://api.codelife.cc/itab/update'


def get_html(url, data):
    try:
        # proxy = { "https": "http://username:password@xxxxxx.com:8080" }
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0'
            ,
                   'token':
                       'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MzA0NDE2Y2MyZjhkMGIyMzZkNjQ4YTUiLCJpYXQiOjE2NjIzNDQ3NDQsImV4cCI6MTY5MzQ0ODc0NH0.HAis5WIOuD6gYmRCCpvhgQ7TERBY2Cd9mHGUSgHvPvo'
                   ,'signaturekey': 'U2FsdGVkX18ASdOzk+oTc84/4w1UM7IxoHIDsdemL+M='}

        requests.options(url)
        r = requests.post(url, timeout=30, headers=headers, data=data)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        print('获取数据失败，请检查你的网络连接')
        print(str(traceback.format_exc()))
        return "ERROR"


def main(base_url):
    data = {"notes": [
        {"id": "8xZAToa5_Kx5TO54hBYzo4317",
         "title": "123",
         "content": "ssssss",
         "fixed": False,
         "ct": 1689669360722,
         "ut": int(time.time()*1000)
         }
    ]}
    json1=json.dumps(data)
    print(json1)
    url = 'https://api.codelife.cc/itab/update'
    html = get_html(url, json1)
    print(html)

    url = 'https://api.codelife.cc/user/update'
    data = {"itabAsyncTime.notes": int(time.time()*1000)}
    json2=json.dumps(data)
    print(json2)
    html2 = get_html(url, json2)
    print(html2)


if __name__ == '__main__':
    main(base_url)
