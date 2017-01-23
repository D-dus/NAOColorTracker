import socket 
from io import BytesIO
from datetime import datetime
import time
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math


def nothing(x):
	pass

def FindTheCenterOfTheColoredTarget(iImage,iColorUpperBound,iColorLowerBound):
	oImage=iImage.copy()
	blur=cv2.blur(iImage,(5,5))
	hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
	mask=cv2.inRange(hsv,iColorLowerBound,iColorUpperBound)
	mask = cv2.erode(mask, None, iterations=1)
	mask = cv2.dilate(mask, None, iterations=2)
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
	centers = []
	cntsPoly=[]
	radius=[]
	boundrects=[]
	if len(cnts) > 0:
		for cnt in cnts:
			eps=0.1*cv2.arcLength(cnt,True)
			cntPolyTemp=cv2.approxPolyDP(cnt,eps,True)
			cntsPoly.append(cntPolyTemp)
			r,c,h,w=cv2.boundingRect(cnt)
			((xTemp, yTemp), radiusTemp)=cv2.minEnclosingCircle(cntPolyTemp)
			centers.append((int(xTemp),int(yTemp)))
			radius.append(radiusTemp)
			boundrects.append((r,c,w,h))
			
	return centers,mask,radius

def Distance(A,B):
	return math.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)

def ReArrangeNaoPosition(CurrentPosition,OldPosition):
	TruePosition=[None]*len(CurrentPosition)
	i=0
	for positionOld in OldPosition:
			MinDistance=10000
			for position in CurrentPosition:
				
				if Distance(positionOld,position)<MinDistance:
					MinDistance=Distance(positionOld,position)
					TruePosition[i]=position
			i=i+1
	return TruePosition

def DisplayNaoPositionInFrame(frame,Naoposition):	
	ID=0
	for center in NaoPosition:
		if center!=None:
			cv2.circle(frame,center,15,(225,0,0),2)						
			targetName="Target "+str(ID)
			cv2.putText(frame,targetName,(center[0]+17,center[1]),font,0.3,(255,255,255),1,cv2.LINE_AA)
			ID=ID+1
	return frame

if __name__=='__main__':

	#------------------------------- TCP IP Simulation ----------------------------------
	port=4321
	host="127.0.0.1"


	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.bind((host,port))
	sock.listen(1)
	print("Server is listening")
	connection,addrClient=sock.accept()
	#------------------------------------------------------------------------------------


	#------------------------------------Webcam------------------------------------------
	#cap=cv2.VideoCapture(0)
	#------------------------------------------------------------------------------------


	cv2.namedWindow("DebugScreen")
	cv2.namedWindow("Control")

	#-----------------------------------------------------------------------------------
	cv2.createTrackbar('h',"Control",1,180,nothing)
	cv2.createTrackbar('H',"Control",1,180,nothing)
	#-----------------------------------------------------------------------------------

	mIsInit=False
	mIsTracking=False
	font = cv2.FONT_HERSHEY_SIMPLEX
	try:
		while(True):

			H=cv2.getTrackbarPos('H',"Control")
			h=cv2.getTrackbarPos('h',"Control")

			#---------------Simulator-----------------------
			data=connection.recv(1000000)
			npImage=np.frombuffer(data,np.uint8)
			im=cv2.imdecode(npImage,cv2.IMREAD_UNCHANGED)
			#-----------------------------------------------


			#------------------Webcam----------------------
			#ret,im=cap.read()
			#----------------------------------------------
			lBlueUpperBound=(110,255,255)
			lBlueLowerBound=(80,86,6)
			lBlueCenters,lBlueMask,BlueRadius=FindTheCenterOfTheColoredTarget(im,lBlueUpperBound,lBlueLowerBound)			
			if mIsInit:
				NaoPosition=ReArrangeNaoPosition(lBlueCenters,lBlueCentersOld)
				lBlueCentersOld=NaoPosition			
				
				Result=DisplayNaoPositionInFrame(im.copy(),NaoPosition)
	
			##############################Display#############################
		
				cv2.imshow("DebugScreen",Result)
				cv2.waitKey(1)
			messageToSend="Received"
			connection.send(bytes(messageToSend,'utf-8'))
			if not mIsInit:
				lBlueCentersOld=lBlueCenters
				mIsInit=True
			##################################################################		
		connection.close
	except KeyboardInterrupt:
		print("Interrupted")
		connection.close()
