import cv2

# open device
cap = cv2.VideoCapture(-1)

if not (cap.isOpened()):
	print("Could not open video device")

#To set the resolution
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH, 640))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT, 480))

# set up writer
writer = cv2.VideoWriter('samplevideo.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 30, (width,height))
# DIVX is the video codec, works on all platforms


while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	writer.write(frame)

	# Display the resulting frame
	cv2.imshow('preview',frame)

	#Waits for a user input to quit the application
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture 
cap.release()
writer.release()
cv2.destroyAllWindows()
