import cv2 as cv
##read image
img=cv.imread("Kitten.jpeg",cv.IMREAD_COLOR)
cv.imshow("kitten Image", img)
cv.waitKey(0)
cv.destroyAllWindows()
##read video
capture=cv.VideoCapture('videoplayback.mp4')
while True:
    isTrue, frame=capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release
cv.waitKey(0)