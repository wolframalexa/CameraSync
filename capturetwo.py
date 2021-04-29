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
<<<<<<< HEAD
=======
	width = 1920
	height = 1080
	i = 0
>>>>>>> cce58eae6872ae668e6d10efb70482edb35594f0

	cam = cv2.VideoCapture('v4l2src device=/dev/video' + str(camID) + ' io-mode=2 ! image/jpeg, width=(int)1920, height=(int)1080 ! jpegdec ! video/x-raw ! videoconvert ! video/x-raw,format=BGR ! appsink', cv2.CAP_GSTREAMER)
	writer = cv2.VideoWriter('004_video1.mp4v', cv2.VideoWriter_fourcc(*'mp4v'), 30, (width,height))

	frameRate = cam.get(5)

	if not cam.isOpened():
		print("Could not open camera")

	while True:
		rval, frame = cam.read()
		writer.write(frame)
<<<<<<< HEAD
		cv2.imshow(previewName,frame)
=======
		cv2.imshow(previewName, frame)
>>>>>>> cce58eae6872ae668e6d10efb70482edb35594f0

		frameId = cam.get(1)
		if (frameId % int(frameRate) == 0):
			filename = "captures/004_image_" + str(int(frameId)) + ".jpg"
<<<<<<< HEAD
			cv2.imwrite(filename,frame)
=======
			cv2.imwrite(filename, frame)

>>>>>>> cce58eae6872ae668e6d10efb70482edb35594f0
			timearray[i] = time.time() - starttime
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


thread1.exit()
thread2.exit()

# write data
<<<<<<< HEAD
f = open("004d_timedata.txt",'a')
f.write(str(time1.timearray)
f.write(str(time2.timearray))
f.close()
=======
f = open("004d_timedata.txt",'w')
print(thread1.timearray)
print(thread2.timearray)
#f.write(str(thread1.timearray))
#f.write(str(thread2.timearray))
#f.close()
>>>>>>> cce58eae6872ae668e6d10efb70482edb35594f0
