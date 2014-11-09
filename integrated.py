#Integrated
#James horrible hacked attempt to find barcodes.

import cv2
import math
import zbar
from PIL import Image , ImageDraw

scanner = zbar.ImageScanner()
scanner.parse_config('enable')

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()

    #cv2.imwrite("picture.jpg",frame)
    pil_im = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    pil_im = Image.fromarray(pil_im)

    draw = ImageDraw.Draw(pil_im)

    width, height = pil_im.size
    converted = pil_im.convert('L')
    raw = converted.tostring()
    #was y800.
    forScanner = zbar.Image(width, height, "Y800", raw)
    scanner.scan(forScanner)

    for symbol in forScanner:
          # So we get some numbers out, not really sure what they are. Might as well draw some lines and see what happens.
          #I think the longest line should be our "best" match... but why can't it give us a bounding box or something! Nuts.

          print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
          """
          # clean up
          [a,b,c,d] = symbol.location   # it returns the four corners of the QR code in an order
          w = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)  # Just distance between two points
          h = math.sqrt((b[0]-c[0])**2 + (b[1]-c[1])**2)
          Area = w*h

          draw.line([a,b])
          """

          pairs = len(symbol.location)
          print pairs
          for x in range(pairs):
            print symbol.location[x], symbol.location[x-1]
            draw.line([symbol.location[x], symbol.location[x-1]])
            pil_im.save("drawn.png","PNG")

              #don't uncomment or the screen fills up with pictures.
    #pil_im.show()

    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        cv2.imwrite("picture.jpg",frame)
        break
cv2.destroyWindow("preview")
