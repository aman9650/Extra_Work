import cv2
import numpy as np
'''
img=cv2.imread("mountain-landscape-2031539_640 (1).jpg")
cv2.imshow("window",img)
cv2.waitKey(0)

cap=cv2.VideoCapture('')

# video is series of images
while True:
    success, img=cap.read()
    cv2.imshow("window",img)
    if cv2.waitKey(1) & 0xFF ==ord('q')
        break

cap=cv2.VideoCapture(0)
cap.set(3,640) #width id 3
cap.set(4,480) # height id 4

cap.set(10,100) # for brightness
# video is series of images
while True:
    success, img=cap.read()
    cv2.imshow("window",img)
    if cv2.waitKey(1) & 0xFF ==ord('x'):
        break
'''

# Basic functions
'''
img=cv2.imread("mountain-landscape-2031539_640 (1).jpg")
kernel=np.ones((5,5),np.uint8)
# convert to greyscale
imgGrey=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

imgBlur=cv2.GaussianBlur(imgGrey,(7,7),0)

imgCanny=cv2.Canny(img,100,200)

imgDialation=cv2.dilate(imgCanny,kernel,iterations=1)

imgErode=cv2.erode(img,kernel,iterations=1)
cv2.imshow("window",imgErode)
cv2.waitKey(0)
'''


##  Resizing and cropping
'''
img=cv2.imread("pink-324175_640.jpg")
print(img.shape)

imgResize=cv2.resize(img,(500,400))
imgCropped=img[0:300,0:500] # hight:width
cv2.imshow("window1",imgCropped)
cv2.imshow("window",imgResize)
cv2.waitKey(0)

'''
# Shapes and texts
'''
img = np.zeros((512,512,3),np.uint8) # zeroes means black [height,width,channel]
print(img)
## img[200:300,100:300]=255,0,0  # malking specific part blue
cv2.line(img,pt1=(0,0),pt2=(img.shape[0],img.shape[1]),color=(0,255,0),thickness=3)

cv2.rectangle(img,(0,0),(250,350),(0,0,255),2) # to fill rectangle put thikness= -1

cv2.circle(img,(400,50),radius=50,color=(255,255,0),thickness=2)

cv2.putText(img,'OPencv',(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),2)
cv2.imshow("window",img)
cv2.waitKey(0)

'''
# Wrap Perspective
'''
img=cv2.imread("pink-324175_640.jpg")
width,height=250,350
pts1=np.float32([[111,219],[287,188],[154,482],[352,440]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)

imgOutput=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("window",imgOutput)
cv2.waitKey(0)
'''
# Joining Images

img = cv2.imread("mountain-landscape-2031539_640 (1).jpg")
imghor=np.hstack((img,img))
imgvir=np.vstack((img,img))
cv2.imshow("window",imghor)
cv2.imshow("window2",imgvir)
cv2.waitKey(0)
