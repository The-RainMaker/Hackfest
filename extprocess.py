#!/usr/bin/env python

import subprocess
from pprint import pprint

## get video duration
#ps   = subprocess.Popen(('omxplayer', '-i', '/home/pi/Videos/Xbox One S.mp4'), stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
#try:
#	meta = subprocess.check_output(('sh', '-c', 'grep', '-i', 'duration', '|', 'awk', '{ print $2 }'), stdin = ps.stdout)
#except Exception as e:
#	print("[Errno {0}] {1}".format(e.returncode, e.output))
##duration = subprocess.check_output(('awk', '{ print $2 }'), stdin = meta.stdout)
#ps.wait()
##print meta

def convert_to_seconds(time_str):
	h, m, s = time_str.split(':')
	return int(h) * 3600 + int(m) * 60 + int(s)

videoDir = '/home/pi/Videos/'
video = videoDir + 'Xbox One S.mp4'
#meta = subprocess.check_output(('sh', '-c', 'omxplayer', '-i', '/home/pi/Videos/Xbox One S.mp4', '|', 'grep', '-i', 'duration', '|', 'awk', '{ print $2 }'))
#meta = subprocess.check_output(('sh', '-c', 'omxplayer -i "/home/pi/Videos/Xbox One S.mp4" 2>&1 | grep -i duration | awk \'{ print $2 }\''))
#extCommand = 'omxplayer -i "' + video + '" 2>&1 | grep -i duration | awk \'{ print $2 }\'';
extCommand = "omxplayer -i '" + video + "' 2>&1 | grep -i duration | awk '{ print $2 }'";
meta = subprocess.check_output(('sh', '-c', extCommand))
# remove whitespaces
duration = meta.strip()
# 00:01:42.96, -> 00:01:42
duration = duration[:-4]
print duration
# get duration in seconds
duration = convert_to_seconds(duration)
print duration
player = subprocess.Popen(('omxplayer', video))
player.wait()

#try:
#	#subprocess.check_output(['omxplayer', '-i', '/home/pi/Videos/Xbox One S.mp4'], stderr = subprocess.STDOUT)
#	ps = subprocess.Popen(('omxplayer', '-i', '/home/pi/Videos/Xbox One S.mp4'), stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
#except Exception as e:
#	# funny things happen here, the omxplayer command will return 1 if success while subprocess will consider it as error
#	print("[Errno {0}] {1}".format(e.returncode, e.output))
#	output = subprocess.check_output(('grep', '-i', 'duration'), stdin = ps.stdout)
#	print output



#ps = subprocess.Popen(('ps', '-A'), stdout=subprocess.PIPE)
#output = subprocess.check_output(('grep', 'process_name'), stdin=ps.stdout)
#ps.wait()
#
