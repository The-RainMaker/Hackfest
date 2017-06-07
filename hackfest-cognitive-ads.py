#!/usr/bin/env python

# ----------------------------------------------------------------------------#
# $Id: hackfest-cognitive-ads.py Exp $                                        #
# $Id: Last modified on 2017-06-06 Exp $                                      #
# $Id: Microsoft - Developer eXperience Team Exp $                            #
# $Id: The RainMaker (faizalm at microsoft dot com) Exp $                     #
# ----------------------------------------------------------------------------#

import base64, httplib, json, urllib
import picamera, random, signal, subprocess, sys
from time import sleep, strftime

# ----------------------------------------------------------------------------#
# variables
# ----------------------------------------------------------------------------#
videoDir      = '/home/pi/Videos/'
capturedImage = '/home/pi/Desktop/TRM.jpg'
# camera properties
camera            = picamera.PiCamera()
camera.brightness = 60
camera.rotation   = 180
camera.hflip      = True
camera.resolution = (1024, 768)
camera.framerate  = 24
# for annotation
camera.annotate_background = picamera.Color('black')
camera.annotate_foreground = picamera.Color('white')
camera.annotate_text_size  = 40
camera.annotate_text       = " --- DX Cognitive Services Hackfest --- "
# azure cognitive services properties
headers = {
	'Content-Type': 'application/octet-stream',
	'Ocp-Apim-Subscription-Key': 'ec6669490c644082b4311d09db20c9b2',
}

params = urllib.urlencode({
	'visualFeatures': 'Categories,Description,Faces',
})

# ----------------------------------------------------------------------------#
# supporting functions
# ----------------------------------------------------------------------------#
def ConvertToSeconds(timeStr):
	h, m, s = timeStr.split(':')
	return int(h) * 3600 + int(m) * 60 + int(s)

def AnalyzeImage(image):
	with open(image, "rb") as imgFile:
		imgStream = imgFile.read()
	body = imgStream
	data = '{}'

	try:
		conn     = httplib.HTTPSConnection('southeastasia.api.cognitive.microsoft.com')
		conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
		response = conn.getresponse()
		data     = response.read()
		conn.close()
	except Exception as e:
		print("[Errno {0}] {1}".format(e.errno, e.strerror))
	return data

def signal_handler(signal, frame):
	print (strftime("%Y-%m-%d %H:%M:%S")) + " Program exit"
	camera.close()
	sys.exit(0)

# ----------------------------------------------------------------------------#
# main code
# ----------------------------------------------------------------------------#
signal.signal(signal.SIGINT, signal_handler)
video = videoDir + 'Microsoft Build 2017 Azure Customers.mp4'

while True:
	# get video duration
	extCmd   = "omxplayer -i '" + video + "' 2>&1 | grep -i duration | awk '{ print $2 }'";
	meta     = subprocess.check_output(('sh', '-c', extCmd))
	# remove whitespaces
	duration = meta.strip()
	# 00:01:42.96, -> 00:01:42
	duration = duration[:-4]
	# get duration in seconds
	duration = ConvertToSeconds(duration)

	# start playing first video
	player = subprocess.Popen(('omxplayer', video))
	# sleep until 15 seconds before video end then capture image
	sleep(duration - 15)
	print (strftime("%Y-%m-%d %H:%M:%S")) + " Capturing image"
	camera.capture(capturedImage)
	print (strftime("%Y-%m-%d %H:%M:%S")) + " Analyzing image"
	data   = AnalyzeImage(capturedImage)
	parsed = json.loads(data)
	print json.dumps(parsed['faces'], indent = 4)

	# do something with image analysis result - http://socialmarketing.org/archives/generations-xy-z-and-the-others/
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
		# any generation Z out there?
		video = videoDir + 'Xbox One S.mp4'
		print (strftime("%Y-%m-%d %H:%M:%S")) + " Hiya Gen Z!"
	elif (genYCount >= 1):
		# this actually should be if genYCount more than genXCount
		video = videoDir + 'Microsoft Power BI in 60 Seconds.mp4'
		print (strftime("%Y-%m-%d %H:%M:%S")) + " Ay ay ay, Gen Y eh"
	elif (femaleCount >= 1):
		# this should be like if female more than male
		video = videoDir + 'Microsoft Surface Laptop Commercial.mp4'
		print (strftime("%Y-%m-%d %H:%M:%S")) + " Lots of ladies here!"
	else:
		# pick random video
		videoFiles = [ 'Introducing Office 365 Business.mp4',
					   'Microsoft Vision for Azure Machine Learning.mp4',
					 ]
		video  = videoDir + random.choice(videoFiles)
		print (strftime("%Y-%m-%d %H:%M:%S")) + " Playing random videos for most random generation"

	player.wait()

