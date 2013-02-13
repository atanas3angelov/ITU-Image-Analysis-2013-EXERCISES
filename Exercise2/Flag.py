from pylab import *
import cv2 

#----------------------------Functions
def GetCoordinates(I):
    fig = figure(1)
    gray()
    imshow(I)
    
    fig.hold('on')
    X = ginput(2)
    print list(X)
    
    for (x,y) in X:            
        plt.plot(x,y)

    show(False)
    return X

def showFigures(**imgs):
    figure()
    gray()
    
    for (counter, (k,v)) in enumerate(imgs.items()):
        subplot(1,len(imgs) ,counter);imshow(v);title(k)

    show()
#----------------------------------Main body
I=cv2.imread("Flag.jpg")
I=cv2.cvtColor(I, cv2.COLOR_RGB2BGR)
showFigures(flag=I)