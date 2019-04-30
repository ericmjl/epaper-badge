from PIL import Image

def read_img(fname):
    b = Image.open("images/{fname}_b.bmp".format(fname=fname))
    r = Image.open("images/{fname}_r.bmp".format(fname=fname))
    return b, r


def display(fname, epd):
    b, r = read_img(fname)
    epd.Clear(0xFF)
    epd.display(epd.getbuffer(b), epd.getbuffer(r))
    epd.sleep
