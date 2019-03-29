import cv2

face = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
camera = cv2.VideoCapture(0)
cv2.namedWindow('camera')

while True:
    ret, frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = face.detectMultiScale(gray, scaleFactor=1.15, minNeighbors=5, minSize=(5, 5))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('camera', frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
