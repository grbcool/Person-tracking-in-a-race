import cv2
import argparse
import imutils

ap = argparse.ArgumentParser()
ap.add_argument('-i','--video',required=True,help='path to video')
args = vars(ap.parse_args()) 

list_points =[]

def CallBackFunc(event,x,y,flag,param):
	if event==cv2.EVENT_LBUTTONDOWN or event==cv2.EVENT_RBUTTONDOWN :
		list_points.append([x,y])



cam = cv2.VideoCapture(args['video'])

success = True
lastf = None
while success:
	success,frame = cam.read()
	if success == False:
		continue
	frame = imutils.resize(frame,width=500)
	cv2.imshow('Video',frame)
	if frame is not None:
		lastf = frame
	cv2.waitKey(1)
	#if cv2.waitKey(1)==ord('q'):
	#	break
	
cv2.imwrite('lasti.jpg',lastf)	
cv2.namedWindow('MouseCallback')
cv2.setMouseCallback('MouseCallback',CallBackFunc)

img = cv2.imread('lasti.jpg')
while True:
	cv2.imshow('MouseCallback',img)
	if len(list_points)==2:
		break
	if cv2.waitKey(1) & 0xFF ==ord('q'):
		break	

	
			
	
print(list_points)			
