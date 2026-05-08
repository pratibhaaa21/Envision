from PIL import Image , ExifTags
img1 = Image.open("Task 2/2.3/image2.jpg")
img2 = Image.open("Task 2/2.3/image2.png")
exif_data1 = img1._getexif()
exif_data2 = img2._getexif()

if exif_data1 is None:
    print ("Data1 is not found .")
else :
    for (exif_tag , value) in exif_data1.items():
        exif_name = ExifTags.TAGS.get(exif_tag , "unknown")
        print(exif_name , exif_tag , value)

if exif_data2 is None:
    print("Data2 is not found. ")
else:
    for (exif_tag , value)  in exif_data2.items():
        exif_name = ExifTags.TAGS.get(exif_tag , "unknown") 
        print(exif_name , exif_tag , value)  