''' notes: jpg doesn't support rgba(transparancy - A: defines opacity of a color)'''
from PIL import Image 
img = Image.open("Task 2/2.1/image1.jpg")
img.save("Task 2/2.1/image1.png")
img.convert("RGB")
