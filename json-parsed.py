#!/usr/bin/env python

import httplib, urllib, base64, json
import random

foo = ['a', 'b', 'c', 'd', 'e']
print(random.choice(foo))

#data = '{"requestId":"11b4c304-1c2d-4768-b141-124969239c9f","metadata":{"width":1024,"height":768,"format":"Jpeg"},"faces":[{"age":36,"gender":"Male","faceRectangle":{"left":457,"top":204,"width":68,"height":68}},{"age":12,"gender":"Male","faceRectangle":{"left":640,"top":106,"width":52,"height":52}}]}'
#data = '{"requestId":"1f7f9569-6c2d-466c-88ad-e6434ab56ba4","metadata":{"width":1024,"height":768,"format":"Jpeg"},"faces":[{"age":28,"gender":"Female","faceRectangle":{"left":575,"top":272,"width":99,"height":99}},{"age":27,"gender":"Male","faceRectangle":{"left":427,"top":208,"width":68,"height":68}}]}'
data = '{"requestId":"e133fa60-d7e8-41a4-be70-2001c1a6a815","metadata":{"width":1024,"height":768,"format":"Jpeg"},"faces":[{"age":38,"gender":"Female","faceRectangle":{"left":449,"top":326,"width":94,"height":94}},{"age":12,"gender":"Male","faceRectangle":{"left":736,"top":366,"width":89,"height":89}},{"age":28,"gender":"Male","faceRectangle":{"left":419,"top":208,"width":68,"height":68}}]}'

parsed = json.loads(data)
#print json.dumps(parsed['faces'], indent = 4)

# http://socialmarketing.org/archives/generations-xy-z-and-the-others/
totalPerson     = 0
femaleCount     = 0
maleCount       = 0
genBoomersCount = 0
genXCount       = 0
genYCount       = 0
genZCount       = 0

for data in enumerate(parsed['faces']):
	totalPerson += 1
	for key, value in data[1].items():
		if (key == 'gender'):
			if (value == 'Female'):
				femaleCount += 1
			else:
				maleCount += 1
		if (key == 'age'):
			if (value >= 52):
				genBoomersCount += 1
			elif (value >= 41):
				genXCount += 1
			elif (value >= 23):
				genYCount += 1
			else:
				genZCount += 1

if (genZCount >= 1):
	print "Got generation Z here!"
