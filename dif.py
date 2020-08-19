from PIL import Image
from pathlib import Path


image1 = open(input("Enter first file name with extension"))
image2 = open(input("Enter second file name with extension"))
# im = Image.new(mode = "RGB", size=(400,400), color=(90, 30, 230))


# name = "generatedImage"
# num = 0
# extension = ".png"
# potentialName = Path(name+str(num)+extension)
# while potentialName.is_file() == True:
#     print("was file")
#     num += 1
#     potentialName = Path(name+str(num)+extension)
# else:
#     print("was not file")
# print("file was named", potentialName)
# im.save(potentialName)
# im.show()