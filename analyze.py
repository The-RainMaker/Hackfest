#!/usr/bin/env python

import httplib, urllib, base64, json

headers = {
	'Content-Type': 'application/octet-stream',
	'Ocp-Apim-Subscription-Key': 'ec6669490c644082b4311d09db20c9b2',
}

# 'visualFeatures': 'Categories,Description,Faces',
params = urllib.urlencode({
	'visualFeatures': 'Faces',
})

with open("/home/pi/Desktop/TRM-03.jpg", "rb") as imgFile:
	imgStream = imgFile.read()
	#imgStream = base64.b64encode(imgFile.read())
#body = "{" + "{0}".format(imgStream) + "}"
body = imgStream
data = '{}'

try:
	conn = httplib.HTTPSConnection('southeastasia.api.cognitive.microsoft.com')
	conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
	response = conn.getresponse()
	data = response.read()
	print(data)
	parsed = json.loads(data)
	print json.dumps(parsed, indent = 4)
	conn.close()
except Exception as e:
	print("[Errno {0}] {1}".format(e.errno, e.strerror))
	parsed = json.loads(data)
	print json.dumps(parsed, indent = 4)
