#!/usr/bin/python
import zbar
import math
from PIL import Image , ImageDraw
#filename = "picture.jpg"
filename = "picture.jpg"
#if len(argv) < 2: exit(1)
# create a reader
scanner = zbar.ImageScanner()
# configure the reader
scanner.parse_config('enable')
# obtain image data
pil = Image.open(filename).convert('L')
width, height = pil.size
raw = pil.tostring()
# wrap image data
image = zbar.Image(width, height, 'Y800', raw)
# scan the image for barcodes
scanner.scan(image)
# extract results
draw = ImageDraw.Draw(pil)
for symbol in image:
    # So we get some numbers out, not really sure what they are. Might as well draw some lines and see what happens.
    #I think the longest line should be our "best" match... but why can't it give us a bounding box or something! Nuts.
    print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
    # clean up
    [a,b,c,d] = symbol.location   # it returns the four corners of the QR code in an order
    w = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)  # Just distance between two points
    h = math.sqrt((b[0]-c[0])**2 + (b[1]-c[1])**2)
    Area = w*h

    draw.line([a,b])

    """
    pairs = len(symbol.location)
    for x in range(pairs):
      print symbol.location[x], symbol.location[x-1]
      draw.line([symbol.location[x], symbol.location[x-1]])
  """

pil.show()
pil.save("MarkedUpBarcode.png","PNG")
del(image)
del(draw)


#########

