from time import sleep
from turtle import color
import pyscreenshot as ImageGrab

sleep(5)
def checkColor(x, y):
    im = ImageGrab.grab(bbox=(x, y, x+1, y+1))
    rgbim = im.convert('RGB')
    r,g,b = rgbim.getpixel((0,0))
    color_RGB = [r,g,b]
    return color_RGB

#colour1 = checkColor(945 , 672)
#print(colour1)
