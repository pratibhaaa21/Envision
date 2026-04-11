from PIL import Image
img1 = Image.open("Task 2/2.1/image1.jpg")
img2 = Image.open("Task 2/2.1/image1.png")

size1 = img1.size
size2 = img2.size
print(size1 , size2)

'''png reduces size by compressing the data. So if the data is simple colours , shapes etc , png
compresses it  efficiently . so the size becomes smaller. BUT if the data is a large number of colours
and very compplex designs etc , png keeps everything unchanges . hence the size becomes larger. '''
 
