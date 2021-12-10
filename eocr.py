import cv2
from xlwt import Workbook
import easyocr
import os

def i2t (x):
    reader = easyocr.Reader(['en'])
    results = reader.readtext(x)
    text = ''
    for result in results:
        text += result[1] + ' '

    return text

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
platecascade = cv2.CascadeClassifier("data/haarcascade_russian_plate_number.xml")
frameWidth = 640
frameHeight = 400
address = "sv5.mp4"
vdo = cv2.VideoCapture(address)
vdo.set(3, frameWidth)
vdo.set(4, frameHeight)
# vdo.set(10, 150)
count = 0
# # cp is capture file name sereis
# cp = 1
raw = 0
col = 0
path = 'D:/p_project/ALPR/c_plate'
while True:
    ret, img = vdo.read()
    Gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plates = platecascade.detectMultiScale(Gray, 1.1, 4)
    for (x, y, w, h) in plates:
        area = w * h
        if area > 500:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            plateArea = img[y:y + h, x:x + w]

            # cv2.imwrite(os.path.join(path, f'detect_{cp}.png'), plateArea)
            # cp = cp+1
            text = i2t(plateArea)

            sheet1.write(raw, col, text)
            raw = raw+1


            cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)
            cv2.imshow("live cam", plateArea)
    cv2.imshow("live cam", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        wb.save('xlwt example.xls')
        break
