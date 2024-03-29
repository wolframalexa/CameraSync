import cv2
import time
import numpy as np
from multiprocessing import Process
from queue import Queue

def runCamera(camID, timearray, out_q):
	width = 1920
	height = 1080

	cap = cv2.VideoCapture('v4l2src device=/dev/video' + str(camID) + ' io-mode=2 ! image/jpeg, width=(int)1920, height=(int)1080 ! jpegdec ! video/x-raw ! videoconvert ! video/x-raw,format=BGR ! appsink', cv2.CAP_GSTREAMER)
	writer = cv2.VideoWriter('004_video' + str(camID) + '.mp4v', cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))

	if not cap.isOpened():
		print("Could not open camera")
	frameRate = cap.get(5)

	i = 0
	while(True):
		ret, frame = cap.read()
		writer.write(frame)

		cv2.imshow("Camera 0",frame)

		frameId = cap.get(1)
		if (frameId % int(frameRate) == 0):
			filename = "captures/004_image_" + str(camID) + str(int(frameId)) + ".jpg"
			cv2.imwrite(filename,frame)
			timearray[i] = time.time() - starttime
			i += 1

		if i == n: # exit when array full
			out_q.put(timearray)
			break

	cap.release()
	writer.release()
	cv2.destroyAllWindows()

n = 10
time1 = np.zeros((n,1))
time2 = np.zeros((n,1))

results = Queue()

p1 = Process(target = runCamera, args=(0, time1, results,))
p2 = Process(target = runCamera, args=(1, time2, results,))

starttime = time.time()
p1.start()
p2.start()

resultdict = {}
while not results.empty():
	resultdict.update(results.get())

p1.join()
p2.join()
print(resultdict)

# write data
f = open("004d_timedata.txt",'w')
f.write(str(resultdict))
f.close()
