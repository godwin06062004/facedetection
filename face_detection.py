import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
webcam = cv2.VideoCapture(0)

while True:
    _,img = webcam.read()

    img = cv2.flip(img,1)

    img = cv2.resize(img,(0,0),None,2,2)

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.5,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(74,25,8),3)
        
    cv2.imshow("Face detection", img)

    key = cv2.waitKey(10)
    if key == 27:
        break


webcam.release()
cv2.destroyAllWindows()