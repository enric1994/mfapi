# !/usr/bin/env python2
# -*- coding: utf-8 -*-
# (c) Copyright 2019 Enric Moreu. All Rights Reserved.

from flask import Flask, request, send_file
from skimage.io import imread, imsave
import numpy as np
import cv2
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['POST'])
def process_files():

	# Receive the different files and store them in an array
	received_images = []
	images = request.files.to_dict()
	for image in images:
		file_name = images[image].filename
		logging.info('File received: {}'.format(file_name))
		npimg = np.fromfile(images[image], np.uint8)
		decoded_image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
		imageRGB = cv2.cvtColor(decoded_image , cv2.COLOR_BGR2RGB)
		received_images.append(imageRGB)

	# Do some operation using the received files and the parameters
	# e.g. blend the two images using the param1 value (0.5)
	alpha = float(request.args.get('param1'))
	blended = alpha * received_images[0] + (1 - alpha) * received_images[1]
	imsave('/api/tmp/tmp_result.png', blended/255)

	# Return one file and more parameters
	resp = send_file(open('/api/tmp/tmp_result.png'), mimetype='image/png')
	resp.headers['key1'] = 'value1'
	resp.headers['key2'] = 'value2'
	return resp

app.run(host="0.0.0.0", port=5000)