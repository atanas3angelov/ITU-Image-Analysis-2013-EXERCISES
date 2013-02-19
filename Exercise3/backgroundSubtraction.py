from pylab import *
import cv2

#load the video
cap = cv2.VideoCapture("GreenScreen(lowMP4).mp4")
cv2.namedWindow("input")

#Get the first frame and get the video size
f, backGround = cap.read()
(w,h,t)= shape(backGround)

#Load an image as the stationary backGround
backGround=cv2.imread("GreenScreen(lowMP4)_Green.jpg", cv2.COLOR_RGB2GRAY)
backGround=cv2.resize(backGround, (h,w))
#backGround=cv2.cvtColor(backGround, cv2.COLOR_RGB2GRAY)

newBackGround = cv2.imread("GreenScreen(lowMP4)_Background.jpg")
newBackGround = cv2.resize(newBackGround, (h,w))


while(f):
    f, img = cap.read()
    img_backup=copy(img)
    #img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    #img = cv2.subtract(img, backGround) # SUBTRACTONG ONE FROM ANOTHER
    #img = cv2.absdiff(img, backGround)
    #tresh, img1 = cv2.threshold(img, 20, 255, cv2.THRESH_BINARY)
    
    #img = cv2.bitwise_and(img, newBackGround, img1, backGround)
    
    if f==True:
        cv2.imshow("input", img)
        ch = cv2.waitKey(1)
        if ch == 32:#  Break by SPACE key
            break
#--------------------


