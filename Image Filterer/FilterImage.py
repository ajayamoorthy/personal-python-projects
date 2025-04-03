from PIL import Image, ImageFilter

images = ['./test_images/apples.jpg', './test_images/frogwithflowers.jpg', './test_images/kittyinfield.jpg']

def getImage():
    while True:
        whichImage = input("What image do you want to filter? [1, 2, or 3]: ")

        if int(whichImage) in [1, 2, 3]:
            imgToProcess = images[int(whichImage) - 1]
            img = Image.open(imgToProcess)
            print(img.format)
            return img
        else:
            print("Invalid index, try again")

def filterImage(img):
    while True:
        whichFilter = input("Pick a filter [blur, grayscale, sharpen]: ")
        if whichFilter == "blur":
            filtered_img = img.filter(ImageFilter.BLUR)
            filtered_img.save("blurred.png", "png")
            return

        elif whichFilter == "grayscale":
            filtered_img = img.convert('L')
            filtered_img.save("grayscale.png", "png")
            break

        elif whichFilter == "sharpen":
            filtered_img = img.filter(ImageFilter.SHARPEN)
            filtered_img.save("sharpened.png", "png")
            break

        else:
            print("Invalid filter. Pick one of the options.")

img = getImage()
filterImage(img)