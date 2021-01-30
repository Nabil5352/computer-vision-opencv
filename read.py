import cv2 as cv

# img = cv.imread('./images/1-colorful-painting-by-francoise-nielly.jpg')

# cv.imshow('Painting', img)

# cv.waitKey(0)

capture = cv.VideoCapture('videos/world.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Playing', frame)

    if cv.waitKey(20) & 0xff==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
