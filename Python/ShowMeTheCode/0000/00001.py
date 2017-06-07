from PIL import Image, ImageDraw, ImageFont
import sys
import os

def add_num(picPath, num):
    img = Image.open(picPath)
    x, y = img.size
    myfont = ImageFont.truetype('Futura.ttf', x//3)
    ImageDraw.Draw(img).text((2*x/3, 0), str(num), font=myfont, fill='red')
    outfile = os.path.splitext(picPath)[0] + "_with_num.jpg"
    img.save(outfile)
    Image.open(outfile).show()
    os.remove(outfile)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 %s picPath" % sys.argv[0])
        sys.exit(1)
    add_num(sys.argv[1], 9)
