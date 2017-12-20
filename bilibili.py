# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 21:50:45 2017

@author: dell
"""

import requests
import time
url = 'https://api.live.bilibili.com/ajax/msg'

dat = {'roomid':'30493',
       'token':'',
       'csrf_token':''}
       
while True:
    time.sleep(3)
    html1 = requests.post(url, data = dat)
    asd1 = list(map(lambda ii:html1.json()['data']['room'][ii]['text'], range(10)))
    
    time.sleep(5)
    html2 = requests.post(url, data = dat)
    asd2 = list(map(lambda ii:html2.json()['data']['room'][ii]['text'], range(10)))
    asd = list(set(asd1 + asd2))
    
    print(asd)
    
#requests.request('post',url, dat)