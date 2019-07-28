from PIL import Image

import os

def create_border(srcImage):
    
    newWidth = 4000
    newHeight = 4000
    oldWidth, oldHeight = srcImage.size
    im = Image.new('RGB', (newWidth,newHeight))
    
    # paste in center
    xOffset = int(newWidth/2 - oldWidth/2)
    yOffset = int(newHeight/2 - oldHeight/2)
    im.paste(srcImage, (xOffset , yOffset, xOffset+oldWidth, yOffset+oldHeight))
    
    return im 

def shift(im, x, y):
    # x: pos = left shift
    # y: pos = up shift
    a = 1
    b = 0
    c = x #left/right (i.e. 5/-5)
    d = 0
    e = 1
    f = y #up/down (i.e. 5/-5)
    im = im.transform(im.size, Image.AFFINE, (a, b, c, d, e, f))
    
    return im

# newImage = Image.new(mode, (newWidth,newHeight))
# newImage.paste(srcImage, (x1,y1,x1+oldWidth,y1+oldHeight))

def get_data(csvfile):
    import csv
    with open(csvfile, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for file,w,h,x,y in spamreader:
            # print(file,w,h,x,y)
            yield file, int(w), int(h), int(x), int(y)
            

if __name__ == "__main__":

    # coordsfile = r"C:\Temp\KVR\andi on bike selection 1\cycling\cycle away\1\coords.txt"
    # coordsfile = r"C:\Temp\KVR\andi on bike selection 1\cycling\cycle away\2\coords.txt"
    coordsfile = r"C:\Temp\KVR\andi on bike selection 1\cycling\cycle away\3\coords.txt"
    # coordsfile = r"C:\Temp\KVR\andi on bike selection 1\cycling\cycle towards\coords.txt"
    for file,w,h,x,y in get_data(coordsfile):
    # for file,w,h,x,y in get_data(r"C:\Temp\KVR\andi on bike selection 1\cycling\cycle towards\coords.txt"):
        print(file)
        
        # srcImage = Image.open(r"C:\Temp\KVR\andi on bike selection 1\cycling\cycle away\1\IMG_20190711_125339774.jpg")
        srcImage = Image.open(file)
        paddedImage = create_border(srcImage)
        
        # if (w > h):
        # xOffset = int( w/2 - (w/2 - x))
        xOffset = -int(w/2 - x)
        # yOffset = int(h/2 - (h/2 - y))
        # yOffset = y
        yOffset = -int(h/2 - y)
        # else:
            # xOffset = y
            # yOffset = x

        print(xOffset)
        print(yOffset)
        # exit()
        shiftedImage = shift(paddedImage, xOffset,yOffset)
        path, name = os.path.split(file)
        
        print(name)
        newfolder = os.path.join(path,"shifted")
        if not os.path.isdir(newfolder):
            os.mkdir(newfolder)
        newfile = os.path.join(newfolder, name)
        shiftedImage.save(newfile)
        # shifted.save("{})