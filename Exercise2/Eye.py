from pylab import *
import cv2 

#----------------------------Functions
#When a double-starred parameter is declared such as $**imgs$, 
#then all the keyword arguments from that point till the end are collected as a dictionary called $'imgs'$.
def showFigures(**imgs):
    figure()
    gray()
    
    for (counter, (k,v)) in enumerate(imgs.items()): #See how to use the $enumerate()$ function for creating a counter in a loop.
        subplot(1,len(imgs)  ,counter);imshow(v);title(k)

    show()
    
def brightPupil(matrix, thx):
    matrix.nonzero()
    
        



#------------------------------Main body

I=cv2.imread("interlacedEye.jpg") # Loading an image using openCV

dark=I[1::2] #[start:end:step]
bright=I[::2]


showFigures(Original_image=I,Dark_image=dark,Bright_image=bright)

