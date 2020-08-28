from PIL import Image
import os
qr = Image.open("smallerQR.png")
qr = Image.open(input("what is the name of the file you want to open? (with extension): "))

dataImage = [[]]
curLine = 0
blackCharacter = " "
whiteCharacter = "█"
QRpixels = qr.load()
i = 0
while i < qr.size[1]:
# for i in range(0, qr.size[0], qr.size[0]// 25):
    j = 0
    while j < qr.size[0]:
    # for j in range(0, qr.size[1], qr.size[1]//25):
        xPos = int(i+(qr.size[1]/ 25)/2)
        yPos = int(j+(qr.size[0]/ 25)/2)
        # print(xPos, yPos)
        if sum(QRpixels[yPos, xPos]) > 500:
            dataImage[curLine].append(blackCharacter)
            dataImage[curLine].append(blackCharacter)
        else:
            dataImage[curLine].append(whiteCharacter)
            dataImage[curLine].append(whiteCharacter)
        j += qr.size[0]/ 25
    curLine += 1
    dataImage.append([])
    i +=qr.size[0]/ 25

for i in dataImage:
    print(*i,sep="")
