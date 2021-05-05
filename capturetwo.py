import cv2
import time
import numpy as np
import multiprocessing import Process


def runCamera(camID, timearray):
	width = 1920
	height = 1080

	cap = cv2.VideoCapture('v4l2src device=/dev/video' + str(camID) + ' io-mode=2 ! image/jpeg, width=(int)1920, height=(int)1080 ! jpegdec ! video/x-raw ! videoconvert ! video/x-raw,format=BGR ! appsink', cv2.CAP_GSTREAMER)
	writer = cv2.VideoWriter('004_video' + str(camID) + '.mp4v', cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height)
	frameRate = cap.get(5)

	if not cam.isOpened():
		print("Could not open camera")

	i = 0
	while(True):
		ret, frame = cap.read()
		writer.write(frame)

		cv2.imshow("Camera 0",frame)

		frameId = cam.get(1)
		if (frameId % int(frameRate) == 0):
			filename = "captures/004_image_" + str(camID) + frameId + ".jpg"
			cv2.imwrite(filename,frame)
			timearray[i] = time.time() - starttime
			i += 1

		if i == n: # exit when array full
			break

	cap.release()
	writer.release()
	cv2.destroyAllWindows()


n = 10
time1 = np.zeros((n,1))
time2 = np.zeros((n,1))

p1 = Process(target = runCamera, args=(0, time1,))
p2 = Process(target = runCamera, args=(1, time2,))

starttime = time.time()
p1.start()
p2.start()

p1.join()
p2.join()

# write data
f = open("004d_timedata.txt",'w')
f.write(str(time1))
f.write(str(time2))
f.close()
