#James horrible hacked attempt to find barcodes.

import cv2
from zxing import *

zx = BarCodeReader()
#barcode = zx.decode(testimage)

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
    #barcode = zx.decode(frame)
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()

    cv2.imwrite("picture.jpg",frame)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("preview")
