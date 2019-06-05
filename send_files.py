# !/usr/bin/env python2
# -*- coding: utf-8 -*-
# (c) Copyright 2019 Enric Moreu. All Rights Reserved.

import requests
 
url = 'http://localhost:5000/'

content_type = 'multipart/form-data'

files=dict(img1=open('img1.png'),img2=open('img2.png'))

print('waiting respose...')

payload = {'blending': '0.5', 'key2': ['value2', 'value3']}

response = requests.post(url, params=payload, files=files)

with open('result.png', 'wb') as f:
    f.write(response.content)