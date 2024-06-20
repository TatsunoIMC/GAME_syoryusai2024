import cv2 , time
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Webcam Live', frame)
        key = cv2.waitKey(1) & 0xFF
        cascade = cv2.CascadeClassifier('cascade.xml')
        gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        objects =cascade.detectMultiScale(gray, scaleFactor=1.01,minNeighbors=3)
        for(x,y)in objects,:
             cv2.rectangle(frame,(x,y),(0,200,0),thickness=3)
             cv2.imwrite("result.jpg",frame)
             cv2.imshow('image',frame)
    if  key == ord('q'):
               break
cap.release()
cv2.destroyAllWindows()