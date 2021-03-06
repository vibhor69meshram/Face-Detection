import cv2
import numpy as np

face = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
font = cv2.FONT_HERSHEY_SIMPLEX

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)        ##Set camera resolution
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while 1:
    ret, frame = cap.read()         ##Read image frame
    frame = cv2.flip(frame, +1)     ##Mirror image frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detect_face = face.detectMultiScale(gray, 1.2, 1)
    for(x, y, z, h) in detect_face:
        cv2.rectangle(frame, (x, y), (x+z, y+h), (0, 255, 0), 2)
        ROI = gray[x:x+z, y:y+h]
        length = ROI.shape[0]
        breadth = ROI.shape[1]
        Area = length * breadth
        Distance = 3 * (10 ** (-9)) * (Area ** 2) - 0.001 * Area + 108.6
        display = 'Distance = ' + str(Distance)
        ##display = 'Area = ' + str(Area)
        if Area > 0:
            cv2.putText(frame, display, (5, 50), font, 2, (255, 255, 0), 2, cv2.LINE_AA)

    if not ret:                     ##If frame is not read then exit
        break
    if cv2.waitKey(2) == ord('s'):  ##While loop exit condition
        break

    cv2.imshow('Original Image', frame)

cap.release()                   ##Release memory
cv2.destroyAllWindows()         ##Close all the windows