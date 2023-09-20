import os 
from PIL import Image,ImageDraw, ImageChops
from tqdm import tqdm
#To make the program work, run the python script from the directory the directly contains this script, in that directory place a src folder with the other images
imFiles = os.listdir("src")
imgRGB = []
for i in imFiles:
    im = Image.open(f"src\{i}")
    r = 0
    g = 0
    b = 0
    pixels = im.load()
    width, height = im.size
    total = 0
    for x in range(width):
        for y in range(height):
            pix = pixels[x,y]
            pixR,pixG,pixB = pix
            r += pixR
            g += pixG
            b += pixB
            total += 1
    r /= total
    g /= total
    b /= total
    imgRGB.append({"R":r,"G":g,"B":b,"IM":im})
def findClosestRGB(r,g,b):
    closest = 9999
    closestIm = None
    for im in imgRGB:
        d = abs(im["R"]-r)+abs(im["R"]-r)+abs(im["R"]-r)
        if d < closest:
            closest = d
            closestIm = im
    return closestIm
sclFactor = 8
#filename goes here:
originalIm = Image.open("troll.png").convert("RGB")
w,h = originalIm.size
resizeFactor = 12
originalIm = originalIm.resize((w*resizeFactor,h*resizeFactor))
w*=resizeFactor
h*=resizeFactor
originalPix = originalIm.load()

zoomFactor = 8

reconstructed = Image.new('RGB', (w*zoomFactor,h*zoomFactor))

for x in tqdm(range(0,w,sclFactor)):
    for y in range(0,h,sclFactor):
        pix = originalPix[x,y]
        closestIm = findClosestRGB(pix[0],pix[1],pix[2])
        resized = closestIm["IM"].resize((sclFactor*zoomFactor,sclFactor*zoomFactor))
        reconstructed.paste(resized,(x*zoomFactor,y*zoomFactor))
reconstructed.save("Beauty2.png")
reconstructed.show()