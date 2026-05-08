from PIL import Image , ExifTags
img = Image.open("Task 2/2.3/image2.jpg")
exif_data = img._getexif()

if exif_data is None:
    print("No EXIF Data .")
else:
    for (tag_id , value) in exif_data.items():
        tag_name = ExifTags.TAGS.get(tag_id , "unknown")    # ExifTags.Tags() will give the Tag Name corresponding the Tag Id . # .get(-- , "unknown ") means if no tag name corresponding to the tag id exists , it will return "unknown".  
        print(tag_name, tag_id , value)
