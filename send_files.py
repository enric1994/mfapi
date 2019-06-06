# !/usr/bin/env python2
# -*- coding: utf-8 -*-
# (c) Copyright 2019 Enric Moreu. All Rights Reserved.

import requests

# Load multiple files
files=dict(img1=open('img1.png'),img2=open('img2.png'))

# Create some parameters
payload = {'param1': '0.5', 'param2': ['value2.1', 'value2.2']}

# Send files and parameters
response = requests.post('http://localhost:5000/',
    params=payload,
    files=files)

# Save the received file
with open('response_file.png', 'wb') as f:
    f.write(response.content)

# Print the received parameters
print(response.headers.get('key1'))
print(response.headers.get('key2'))
