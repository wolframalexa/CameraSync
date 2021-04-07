import cv2
import math
import time
import numpy as np

n = 100000
time1 = np.zeros((n,1))
time2 = np.zeros((n,1))

# open device
camera1 = cv2.VideoCapture('v4l2src device=/dev/video0 io-mode=2 ! image/jpeg, width=(int)1920, height=(int)1080 ! jpegdec ! video/x-raw ! videoconvert ! video/x-raw,format=BGR ! appsink', cv2.CAP_GSTREAMER)
camera2 = cv2.VideoCapture('v4l2src device=/dev/video1 io-mode=2 ! image/jpeg, width=(int)1920, height=(int)1080 ! jpegdec ! video/x-raw ! videoconvert ! video/x-raw,format=BGR ! appsink', cv2.CAP_GSTREAMER)

if not (camera1.isOpened()):
	print("Could not open camera 1")
if not (camera2.isOpened()):
	print("Could not open camera 2")


#To get the resolution
width = int(camera1.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(camera1.get(cv2.CAP_PROP_FRAME_HEIGHT))

# get frame rate
frameRate1 = camera1.get(5)
frameRate2 = camera2.get(5)

# set up writer
writer1 = cv2.VideoWriter('003_video1.mp4v', cv2.VideoWriter_fourcc(*'mp4v'), 30, (width,height))
writer2 = cv2.VideoWriter('003_video2.mp4v', cv2.VideoWriter_fourcc(*'mp4v'), 30, (width,height))

i = 0
starttime = time.time()
while(True):
	# Capture frame-by-frame
	ret1, frame1 = camera1.read()
	time1[i] = time.time() - starttime
	writer1.write(frame1)

	ret2, frame2 = camera2.read()
	time2[i] = time.time() - starttime
	writer2.write(frame2)

	# Display the resulting frame
	cv2.imshow('preview1',frame1)
	cv2.imshow('preview2',frame2)

	i +=1

	#Waits for a user input to quit the application
	if i == n | (cv2.waitKey(1) & 0xFF == ord('q')):
		endtime = time.time()
		break

camera1.release()
camera2.release()

writer1.release()
writer2.release()

cv2.destroyAllWindows()

f = open("003d_timedata.txt",'a')
f.write(str(time1))
f.write(str(time2))
f.write("Start time: " + str(starttime))
f.write("End time: " + str(endtime))
f.close()
