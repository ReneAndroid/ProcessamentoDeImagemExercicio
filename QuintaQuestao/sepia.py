import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image


def filter_name(img):

    width,height=img.size
    new_img=img.copy()

    for x in range (width):
        for y in range(height):

            red,green,blue=img.getpixel((x,y))
            new_val=(0.3*red+0.59*green+0.11*blue)

            new_red=int(new_val*2)
            if new_red>255:
                new_red=255
                new_green = int(new_val * 1.5)
            if new_green>255:
                new_green=255
                new_blue = int(new_val)
            if new_blue>255:
                new_blue=255


            new_img.putpixel((x,y),(new_red,new_green,new_blue))
            
                

    return new_img


if __name__=="__main__":

    img = Image.open('sepia.png')

    new_img=filter_name(img)

    new_img.save('OutputImage.png')

    new_img.show("OutputImage")
