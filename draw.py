import cv2 as cv
import numpy as np
blank=np.zeros((800,800,3),dtype='uint8')
# cv.imshow("blank",blank)
# blank[200:300,300:400]=0,255,0
# cv.imshow("Green color", blank)

#to draw a rectangle
# cv.rectangle(blank, (10,10),(blank.shape[1]//2, blank.shape[0]//2), (250,250), (0,255,0), thickness=cv.FILLED)
# cv.imshow("rectangle", blank)
# cv.waitKey(0)
# cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255), thickness=3)
# cv.imshow("Circle",blank)


# ##to draw a line
# cv.line(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=3)
# cv.imshow("Line",blank)
# cv.waitKey(0)

#write text
cv.putText(blank,'My name is Mohini Mehta', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0,(0,255,0), thickness=2)
cv.imshow("Text",blank)
cv.waitKey(0)