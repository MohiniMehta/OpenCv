import cv2 as cv
img=cv.imread("Kitten.jpeg",cv.IMREAD_COLOR)
new_width = 500
new_height = 400

# Resize the image
resized_img = cv.resize(img, (new_width, new_height))
cv.imshow("kitten resized Image", resized_img)
cv.waitKey(0)
cv.destroyAllWindows()


##TO resize the video
def rescale(frame, scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
capture=cv.VideoCapture('videoplayback.mp4')
while True:
    isTrue, frame=capture.read()
    frameresized=rescale(frame)

    cv.imshow('Video resized',frameresized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release
cv.waitKey(0)