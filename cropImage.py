from PIL import Image
# imageName = input("Enter image name with file extension: ")
imageName = "generatedImage.png"
im = Image.open(imageName)
startX = int(input("Enter start X: "))
startY = int(input("Enter start Y: "))
width = int(input("Enter width: "))
height = int(input("Enter height: "))

cropped = im.crop((startX, startY, width, height))
newImageName = input("Enter new image name with extension: ")
cropped.save(newImageName)