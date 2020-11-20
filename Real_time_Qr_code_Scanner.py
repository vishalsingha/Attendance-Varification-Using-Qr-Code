import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

with open('Attendence_data.txt') as f:
    mylist = f.read()

while True:
    succes, img = cap.read()
    for barcode in decode(img):
        data = barcode.data.decode('utf-8')
        if data in mylist:
            output = 'Authorized'
            color = (0, 255, 0)
        else:
            output = 'Unauthorized'
            color = (0, 0, 255)
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, color, 5)
        pts2 = barcode.rect
        cv2.putText(img, output, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
        
    cv2.imshow('window', img)
    if cv2.waitKey(30) & 0xff == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
