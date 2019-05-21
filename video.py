import cv2
import time

cv2.namedWindow("Replay, by Iyaz")
vc = cv2.VideoCapture("http://localhost:8082")

if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False

counter = 0

while rval:
    cv2.imshow("Replay, by Iyaz", frame)
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

vc.release()
cv2.destroyWindow("Replay, by Iyaz")
