import cv2 as cv
face_cascade = cv.CascadeClassifier("../haarcascades/haarcascade_frontalface_alt.xml")
cap = cv.VideoCapture(0)
scaling_factor = 1
while True:
    #ret, frame = cap.read()
    frame = cv.imread("../ImageSource/Sample/lena_color.tiff")
    frame = cv.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv.INTER_AREA)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face_rect = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in face_rect:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
    cv.imshow("Face", frame)
    c = cv.waitKey(1)
    if c == 27:
        break
cv.destroyAllWindows()