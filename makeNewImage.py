from PIL import Image
from pathlib import Path
import re


imageSize = input("Enter the x and y image dimensions (both numbers): ")
splitUp=re.split("\W+", imageSize)
splitUp = tuple(map(int, splitUp))
RGBColor = re.split("\W+", input("Enter the RGB color values (all three here): "))
RGBColor = RGBColor + [255]*(3-len(RGBColor))
RGBColor = tuple(map(int, RGBColor))
im = Image.new(mode = "RGB", size=splitUp, color=RGBColor)

name = "generatedImage"
num = 0
extension = ".png"
potentialName = Path(name+str(num)+extension)
while potentialName.is_file() == True:
    print("was file")
    num += 1
    potentialName = Path(name+str(num)+extension)
else:
    print("was not file")
print("file was named", potentialName)
im.save(potentialName)
im.show()