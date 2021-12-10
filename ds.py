from cv2 import cv2
platecascade = cv2.CascadeClassifier("data/haarcascade_russian_plate_number.xml")
frameWidth = 640
frameHeight = 400
address = "sv5.mp4"
vdo = cv2.VideoCapture(address)
vdo.set(3, frameWidth)
vdo.set(4, frameHeight)
vdo.set(10, 150)
count = 0
while True:
    ret, img = vdo.read()
    Gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plates = platecascade.detectMultiScale(Gray, 1.1, 4)
    for (x, y, w, h) in plates:
        area = w * h
        if area > 500:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "number_plate", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)
            plateArea = img[y:y + h, x:x + w]
            cv2.imshow("live cam", plateArea)
    cv2.imshow("live cam", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

