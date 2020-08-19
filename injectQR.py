from PIL import Image
import os

# for f in os.listdir('.'):
#     if f.endswith(".jpg"):
#         # print(f)
#         pass

# name1 = input("Enter image ")
ogPic = Image.open("smallerRed.png")
qr = Image.open("smallerQR.png")
# new1 = image1.crop((0,0, 562, 562))
# new2 = image2.crop((0,0, 562, 562))
# new1.save("smallerRed.png")
# new2.save("smallerQR.png")
pixels = qr.load()
OGpixels = ogPic.load()
# print(tuple(pixels))
for i in range(qr.size[0]):
    for j in range(qr.size[1]):
        # print(pixels[i, j])
        if sum(pixels[i, j]) > 500:
            # print("ran")
            OGpixels[i, j] = (OGpixels[i, j][0], OGpixels[i, j][1]+40, OGpixels[i, j][2])

ogPic.save("outputImage.png")
# out = Image.blend(image1, image2, 0.1)
# out.save("output.png")
# out.show()
# pixels = image1.load()
# # print(pixels[0, 1])
# for i in range(200):
#     pixels[i, 50] = (i*3, 255, 0)
# # pixels.show()
# image1.show()
# image1.save("RBGImage1.jpg")