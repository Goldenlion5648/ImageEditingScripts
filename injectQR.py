from PIL import Image
import os


print("Make sure the QR code image is the same size or smaller than the normal image ")
ogPic = Image.open(input("Enter normal image file name with extension: "))
qr = Image.open(input("Enter QR code file name with extension: "))

xOffset = int(input("Enter x offset to start placing QR code at in normal image "))
yOffset = int(input("Good, now enter y offset to start placing QR code at in normal image "))
boldFactor = int(input("Enter a whole number for how bolded the QR code is in the new image "))
newImageFilename = input("What should the new file be called? ")
QRpixels = qr.load()
OGpixels = ogPic.load()
# print(tuple(QRpixels))
for i in range(qr.size[0]):
    for j in range(qr.size[1]):
        # print(QRpixels[i, j])
        if sum(QRpixels[i, j]) > 500:
            # print("ran")
            OGpixels[i+xOffset, j+yOffset] = (OGpixels[i+xOffset, j+yOffset][0], (OGpixels[i+xOffset, j+yOffset][1]+boldFactor)%256, OGpixels[i+xOffset, j+yOffset][2])

ogPic.save(newImageFilename)
