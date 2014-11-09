#!/usr/bin/python
import zbar
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
    print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
    # clean up
    pairs = len(symbol.location)
    for x in range(3):
      print symbol.location[x], symbol.location[x-1]
      draw.line([symbol.location[x], symbol.location[x-1]])

pil.show()
pil.save("MarkedUpBarcode","PNG")
del(image)
del(draw)
