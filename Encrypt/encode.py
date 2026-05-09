from PIL import Image
img = Image.open("Encrypt/image3.png")
msg = input( "Enter Your Secret Message : ")   # Embedding the secret messgage.
image_mode = img.mode
image_format = img.format
image_size = img.size
print(f"mode = { image_mode}" ) 
print(f"format = {image_format}")
print(f"size = {image_size}")

msg_code = ""

for char in msg:
    letter = format(ord(char) , "08b")
    msg_code+= letter 
msg_code+= str(11111111)  # delimiter ( to define the end of the message . )
print(msg_code) 

pixels = list(img.getdata())

print(len(pixels))    

#for i in range(0,5):
 #   print(pixels[i])

k = 0
modified_pixels = []
for pixel in pixels :
    r , g , b = pixel
    if k < len(msg_code):
        r = (r & ~1) | int(msg_code[k])

    if k + 1 < len(msg_code):
        g = (g & ~1) | int(msg_code[k + 1])

    if k + 2 < len(msg_code):
        b = (b & ~1) | int(msg_code[k + 2])

        new_pixel = (r , g , b)
        modified_pixels.append(new_pixel)
        k+=3
    else:
        break    
      
 

final_pixels = modified_pixels + pixels[len(modified_pixels):]
print(len(final_pixels))

img.putdata(final_pixels)
img.save("Encrypt/modified.png")
