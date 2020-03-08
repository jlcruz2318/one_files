import cv2
# import imutils # For rotating the frame
# import numpy as numpy
# 
# car_cascade = cv2.CascadeClassifier('/home/checkdev/Documents/dev/Environments/open_spot/open_spot/haar_cascade_creation_process/data/cascade.xml')

cap = cv2.VideoCapture(0) #'http://85.237.63.165/mjpg/video.mjpg'

while True:
    ret, img = cap.read()
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # rotated_img = imutils.rotate(gray, -32)
    # cropped_img = rotated_img[200:310, 0:600]
    # cars = car_cascade.detectMultiScale(cropped_img, 2, 5)
    # for (x,y,w,h) in cars:
    #     cv2.rectangle(cropped_img, (x,y), (x+w, y+h), (0,0,255), 2)
    cv2.imshow('Source', img) #cropped_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
