import cv2
import threading
import math
import time
import numpy as np


class camThread(threading.Thread):
	def __init__(self, previewName, camID, timearray, lock):
		threading.Thread.__init__(self)
		self.previewName = previewName
		self.camID = camID
		self.timearray = timearray
		self.lock = lock
	def run(self):
		print("Starting " + self.previewName + "!")
		camPreview(self, lock)


def camPreview(thread_obj):
	previewName = thread_obj.previewName
	camID = thread_obj.camID
	timearray = thread_obj.timearray

	with thread_obj.lock:
		cam = cv2.VideoCapture('v4l2src device=/dev/video' + str(camID) + ' io-mode=2 ! image/jpeg, width=(int)1920, height=(int)1080 ! jpegdec ! video/x-raw ! videoconvert ! video/x-raw,format=BGR ! appsink', cv2.CAP_GSTREAMER)
		writer = cv2.VideoWriter('004_video1.mp4v', cv2.VideoWriter_fourcc(*'mp4v'), 30, (width,height))

	frameRate = cam.get(5)

	if not cam.isOpened():
		print("Could not open camera")

	i = 0
	while True:
		rval, frame = cam.read()
		writer.write(frame)

		with thread_obj.lock:
			cv2.imshow(previewName, frame)

		frameId = cam.get(1)
		if (frameId % int(frameRate) == 0):
			filename = "captures/004_image_" + str(int(frameId)) + ".jpg"
			cv2.imwrite(filename,frame)
			timearray[i] = time.time() - starttime
			i += 1

		if i == n: # exit when array full
			break
	cam.release()
	writer.release()
	cv2.destroyWindow(previewName)

n = 10
time1 = np.zeros((n,1))
time2 = np.zeros((n,1))

lock = threading.Lock()
thread1 = camThread("Camera 1", 0, time1, lock)
thread2 = camThread("Camera 2", 1, time2, lock)

starttime = time.time()
thread1.start()
thread2.start()

thread1.join() # wait until thread executes
thread2.join()

thread1.exit()
thread2.exit()

# write data
f = open("004d_timedata.txt",'w')
f.write(str(time1.timearray))
f.write(str(time2.timearray))
f.close()
