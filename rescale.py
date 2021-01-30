import cv2 as cv

# Reading images
img = cv.imread('./images/1-colorful-painting-by-francoise-nielly.jpg')

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live videos
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

image_resized = rescaleFrame(img)
cv.imshow("Resized image", image_resized)


def changeRes(width, height):
    # Live videos
    capture.set(3, width)
    capture.set(4, height)


# Reading videos
capture = cv.VideoCapture('videos/world.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)

    #cv.imshow('Resized Playing', frame_resized)


    if cv.waitKey(20) & 0xff==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
