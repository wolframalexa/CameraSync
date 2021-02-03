import cv2
import math
import time

def get_time():
        return round(time.time() * 1000)


#imagesFolder = "~/Documents/AutonomyLab/CameraSync/captures"
timestamps = open("timestamps.txt",'a')

# open device
camera1 = cv2.VideoCapture(0)
camera2 = cv2.VideoCapture(1)

if not (camera1.isOpened()):
	print("Could not open camera 1")
if not (camera2.isOpened()):
	print("Could not open camera 2")

# get frame rate
frameRate1 = camera1.get(5)
print("Frame rate for camera 1:", frameRate1)
frameRate2 = camera2.get(5)
print("Frame rate for camera 2:",frameRate2)


#To get the resolution
width = int(camera1.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(camera1.get(cv2.CAP_PROP_FRAME_HEIGHT))

# set up writer
writer1 = cv2.VideoWriter('samplevideocamera1.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 30, (width,height))
writer2 = cv2.VideoWriter('samplevideocamera2.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 30, (width,height))
# DIVX is the video codec, works on all platforms

while(True):
	# Capture frame-by-frame
	ret1, frame1 = camera1.read()
	writer1.write(frame1)

	ret2, frame2 = camera2.read()
	writer2.write(frame2)

	# Display the resulting frame
	cv2.imshow('preview1',frame1)
	cv2.imshow('preview2',frame2)

	# Capture frames every second
	frameId = camera1.get(1) # current frame number
	if (frameId % math.floor(frameRate1) == 0):
		filename1 =  "captures/image_cam1_" + str(int(frameId)) + ".jpg"
		status1 = cv2.imwrite(filename1, frame1)
		timestamps.write(str(get_time()) + "\n")

		filename2 =  "captures/image_cam2_" + str(int(frameId)) + ".jpg"
		status2 = cv2.imwrite(filename2, frame2)
		timestamps.write(str(get_time()) + 2 * "\n")


	#Waits for a user input to quit the application
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture 
camera1.release()
camera2.release()

writer1.release()
writer2.release()

cv2.destroyAllWindows()
timestamps.close()

