from PIL import Image
# changeing the mode and format of the image and checking whether it changes the exif values for the image or not . 
img = Image.open("Task 2/2.3/image2.jpg")
img.convert("1")
img.save("Task 2/2.3/image2.png")
