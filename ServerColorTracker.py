import socket 
from io import BytesIO
from datetime import datetime
import time
import cv2
import numpy as np
import matplotlib.pyplot as plt



def nothing(x):
	pass

def FindTheCenterOfTheColoredTarget(iImage,iColorUpperBound,iColorLowerBound,flag):
	oImage=iImage.copy()
	blur=cv2.blur(iImage,(5,5))
	hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
	mask=cv2.inRange(hsv,iColorLowerBound,iColorUpperBound)
	mask = cv2.erode(mask, None, iterations=1)
	mask = cv2.dilate(mask, None, iterations=2)
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
	center = None
	if len(cnts) > 0:
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
	return center,mask,oImage



################################# TCP IP Simulation #################################
port=4321
host="127.0.0.1"


sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((host,port))
sock.listen(1)
print("Server is listening")
cv2.namedWindow("DebugScreen")
cv2.namedWindow('Control Panel')
connection,addrClient=sock.accept()
#####################################################################################


#####################################################################################
#cap=cv2.VideoCapture(0)
#####################################################################################


######trackbar#########################################
cv2.createTrackbar('b','Control Panel',1,180,nothing)
cv2.createTrackbar('B','Control Panel',1,180,nothing)
cv2.createTrackbar('r','Control Panel',1,180,nothing)
cv2.createTrackbar('R','Control Panel',1,180,nothing)
cv2.createTrackbar('g','Control Panel',1,180,nothing)
cv2.createTrackbar('G','Control Panel',1,180,nothing)
cv2.createTrackbar('y','Control Panel',1,180,nothing)
cv2.createTrackbar('Y','Control Panel',1,180,nothing)
########################################################


	

mListOfNaoCenter=[(0,0),(0,0),(0,0),(0,0)]
font = cv2.FONT_HERSHEY_SIMPLEX
try:
	while(True):

		R=cv2.getTrackbarPos('R','Control Panel')
		r=cv2.getTrackbarPos('r','Control Panel')
		B=cv2.getTrackbarPos('B','Control Panel')
		b=cv2.getTrackbarPos('b','Control Panel')
		G=cv2.getTrackbarPos('G','Control Panel')
		g=cv2.getTrackbarPos('g','Control Panel')
		Y=cv2.getTrackbarPos('Y','Control Panel')
		y=cv2.getTrackbarPos('y','Control Panel')
		###############Simulator#######################
		data=connection.recv(1000000)
		npImage=np.frombuffer(data,np.uint8)
		im=cv2.imdecode(npImage,cv2.IMREAD_UNCHANGED)
		###############################################


		###################Webcam######################
		#ret,im=cap.read()
		###############################################
		lRedUpperBound=(180,255,255)
		lRedLowerBound=(170,86,6)
		lRedCenter,lRedResult,tempR=FindTheCenterOfTheColoredTarget(im,lRedUpperBound,lRedLowerBound,'r')
		mListOfNaoCenter[0]=lRedCenter


		lGreenUpperBound=(70,255,255)
		lGreenLowerBound=(50,86,6)
		lGreenCenter,lGreenResult,tempG=FindTheCenterOfTheColoredTarget(tempR,lGreenUpperBound,lGreenLowerBound,'r')
		mListOfNaoCenter[1]=lGreenCenter
		
		lRGMask=cv2.add(lRedResult,lGreenResult)

		lBlueUpperBound=(110,255,255)
		lBlueLowerBound=(80,86,6)
		lBlueCenter,lBlueResult,tempB=FindTheCenterOfTheColoredTarget(tempG,lBlueUpperBound,lBlueLowerBound,'r')
		mListOfNaoCenter[2]=lBlueCenter

		lRGBMask=cv2.add(lRGMask,lBlueResult)

		lYellowUpperBound=(48,255,255)
		lYellowLowerBound=(28,86,6)
		lYellowCenter,lYellowResult,lResult=FindTheCenterOfTheColoredTarget(tempB,lYellowUpperBound,lYellowLowerBound,'r')
		mListOfNaoCenter[3]=lYellowCenter

		lRGBYMask=cv2.add(lRGBMask,lYellowResult)
		Final=im.copy()
		color=0
		for center in mListOfNaoCenter:
			cv2.circle(Final, center, 5, (0, 0, 0), -1)
			if(color==0):
				cv2.circle(Final,center,15,(255,0,0),2)
				cv2.putText(Final,'Red Target',(center[0]+17,center[1]), font, 0.3,(255,255,255),1,cv2.LINE_AA)
			if(color==1):
				cv2.circle(Final,center,15,(0,255,0),2)
				cv2.putText(Final,'Green Target',(center[0]+17,center[1]), font, 0.3,(255,255,255),1,cv2.LINE_AA)
			if(color==2):
				cv2.circle(Final,center,15,(0,0,255),2)
				cv2.putText(Final,'Blue Target',(center[0]+17,center[1]), font, 0.3,(255,255,255),1,cv2.LINE_AA)
			if(color==3):
				cv2.circle(Final,center,15,(0,255,255),2)
				cv2.putText(Final,'Yellow Target',(center[0]+17,center[1]), font, 0.3,(255,255,255),1,cv2.LINE_AA)
			color=color+1

						

		##############################Display#############################

		cv2.imshow("DebugScreen",Final)
		cv2.waitKey(1)
		messageToSend="Received"
		connection.send(bytes(messageToSend,'utf-8'))	
		print(mListOfNaoCenter)
		##################################################################		
	connection.close
except KeyboardInterrupt:
	print("Interrupted")
	connection.close()
