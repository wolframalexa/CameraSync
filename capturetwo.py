import cv2
import math
import time
import numpy as np

def get_time():
        return round(time.time() * 1000)


#imagesFolder = "~/Documents/AutonomyLab/CameraSync/captures"

n = 100 # timestamp every 0.1 second for an hour
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
writer1 = cv2.VideoWriter('009_video1.mp4v', cv2.VideoWriter_fourcc(*'hevc'), 30, (width,height))
writer2 = cv2.VideoWriter('009_video2.mp4v', cv2.VideoWriter_fourcc(*'hevc'), 30, (width,height))

i = 0
while(True):
	# Capture frame-by-frame
	ret1, frame1 = camera1.read()
#	writer1.write(frame1)

	ret2, frame2 = camera2.read()
#	writer2.write(frame2)

	# Display the resulting frame
#	cv2.imshow('preview1',frame1)
#	cv2.imshow('preview2',frame2)

	# Capture frames every tenth of a second
	frameId1 = camera1.get(1) # current frame number
	frameId2 = camera2.get(1)
	if ((frameId1 * 10) % int(frameRate1) == 0):
#		filename1 =  "captures/004_image1_" + str(int(frameId)) + ".jpg"
#		status1 = cv2.imwrite(filename1, frame1)
		time1[i] = frameId1/frameRate1

#		filename2 =  "captures/004_image2_" + str(int(frameId)) + ".jpg"
#		status2 = cv2.imwrite(filename2, frame2)
		time2[i] = frameId2/frameRate2
		i +=1
		print(i)

	#Waits for a user input to quit the application
	if i == n | (cv2.waitKey(1) & 0xFF == ord('q')):
		break

camera1.release()
camera2.release()

#writer1.release()
#writer2.release()

cv2.destroyAllWindows()

f = open("001d_timedata.txt",'a')
f.write(str(time1))
f.write(str(time2))
f.close()
