import cv2
import threading
import math
import time
import numpy as np


class camThread(threading.Thread):
	def __init__(self, previewName, camID, timearray):
		threading.Thread.__init__(self)
		self.previewName = previewName
		self.camID = camID
		self.timearray = timearray
	def run(self):
		print("Starting " + self.previewName + "!")
		camPreview(self.previewName, self.camID, self.timearray)

def camPreview(previewName, camID, timearray):
	print("In function camPreview")
	width = 1920
	height = 1080
	i = 0
	print(width,height)

#	cv2.namedWindow(previewName)
	print("checkpoint 1")

	cam = cv2.VideoCapture('v4l2src device=/dev/video' + str(camID) + ' io-mode=2 ! image/jpeg, width=(int)1920, height=(int)1080 ! jpegdec ! video/x-raw ! videoconvert ! video/x-raw,format=BGR ! appsink', cv2.CAP_GSTREAMER)
	print("checkpoint 2")

	writer = cv2.VideoWriter('004_video1.mp4v', cv2.VideoWriter_fourcc(*'mp4v'), 30, (width,height))
	print("checkpoint 3")

	frameRate = cam.get(5)
	print("Frame rate: ", frameRate)

	if cam.isOpened(): #try to get first frame
		rval, frame = cam.read()
		starttime = time.time()
	else:
		rval = False

	while rval:
		cv2.imshow(previewName, frame)
		rval, frame = cam.read()
		writer.write(frame)

		frameId = cam.get(1)
		if (frameId % int(frameRate) == 0):
			filename = "captures/004_image_" + str(int(frameId)) + ".jpg"
			timearray[i] = time.time() - starttime
			print("Index of timearray: ", i)
			i += 1

		if i == n: # exit when array full
			endtime = time.time()
			break
	cam.release()
	writer.release()
	cv2.destroyWindow(previewName)

n = 10
time1 = np.zeros((n,1))
time2 = np.zeros((n,1))

thread1 = camThread("Camera 1", 0, time1)
thread2 = camThread("Camera 2", 1, time2)

starttime = time.time()
thread1.start()
thread2.start()


# write data
f = open("004d_timedata.txt",'a')
f.write(str(time1))
f.write(str(time2))
f.close()
