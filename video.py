import cv2
import time

cv2.namedWindow("preview")
vc = cv2.VideoCapture("http://localhost:8082")

if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False

counter = 0

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    time.sleep(0.2)
    if counter >= 150:
        break
    else:
        counter += 1
        print(counter)
    if key == 27: # Esc
        break
cv2.destroyWindow("preview")
