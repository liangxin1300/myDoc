from PIL import Image, ImageDraw, ImageFont
import sys

def add_num(picPath, num):
    img = Image.open(picPath)
    x, y = img.size
    myfont = ImageFont.truetype('Futura.ttf')
    ImageDraw.Draw(img).text((2*x/3, 0), str(num), font=myfont, fill='red')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 %s picPath" % sys.argv[0])
        sys.exit(1)
    add_num(sys.argv[1], 9)
