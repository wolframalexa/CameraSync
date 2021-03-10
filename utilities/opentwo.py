import cv2

# open device
camera1 = cv2.VideoCapture(0)
camera2 = cv2.VideoCapture(1)

if not (camera1.isOpened()):
	print("Could not open camera 1")
if not (camera2.isOpened()):
	print("Could not open camera 2")

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

	#Waits for a user input to quit the application
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture 
camera1.release()
camera2.release()

writer1.release()
writer2.release()

cv2.destroyAllWindows()
