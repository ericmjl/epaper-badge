from PIL import Image
import numpy as np
from pathlib import Path

def open(fname):
    img = Image.open(fname)
    return img


def array(img):
    img_arr = np.array(img)
    return img_arr


def red_array(img_arr):
    r = img_arr[:, :, 0] == 237
    g = img_arr[:, :, 1] == 28
    b = img_arr[:, :, 2] == 36
    return (1 - np.logical_and(r, g, b)) * 255.0

def black_array(img_arr):
    r = img_arr[:, :, 0] == 0
    g = img_arr[:, :, 1] == 0
    b = img_arr[:, :, 2] == 0
    return (1 - np.logical_and(r, g, b)) * 255.0


def save(arr, fname):
    Image.fromarray(arr).resize((384, 640)).convert('RGB').save(fname)



if __name__ == "__main__":
    pngs = Path("images").glob("*.png")


    for png in pngs:
        print('preprocessing ' + str(png))
        img_arr = array(open(png))
        red_arr = red_array(img_arr)
        save(red_arr, str(png).replace('.png', '_r.bmp'))
        blk_arr = black_array(img_arr)
        save(blk_arr, str(png).replace('.png', '_b.bmp'))
