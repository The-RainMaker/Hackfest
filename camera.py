#!/usr/bin/env python

import picamera
import itertools
from time import sleep

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

camera.start_preview()
sleep(10)
camera.capture('/home/pi/Desktop/TRM.jpg')
camera.stop_preview()

#camera.start_preview()
#camera.start_recording('/home/pi/video.h264')
#sleep(10)
#camera.stop_recording()
#sleep(10)
#camera.capture('/home/pi/TRM.jpg')

#annotation = "DX Cognitive Services Hackfest --- "
#camera.annotate_text = ' ' * 36
#camera.annotate_background = picamera.Color('black')
#for c in itertools.cycle(annotation):
#	camera.annotate_text = camera.annotate_text[1:36] + c
#	sleep(0.1)
#camera.stop_preview()



#import picamera
#import datetime as dt
#
#camera = picamera.PiCamera(resolution=(1280, 720), framerate=24)
#camera.start_preview()
#camera.annotate_background = picamera.Color('black')
#camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#camera.start_recording('timestamped.h264')
#start = dt.datetime.now()
#while (dt.datetime.now() - start).seconds < 30:
#    camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#    camera.wait_recording(0.2)
#camera.stop_recording()
