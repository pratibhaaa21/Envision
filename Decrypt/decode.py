from PIL import Image
img = Image.open("Encrypt/modified.png")
img.convert("RGB")
pixels = list(img.getdata())
#print(pixels[:3])
#print(len(pixels))
encoded = []
for pixel in pixels :
    r , g , b = pixel
    r = r & 1
    g = g & 1
    b = b & 1
    new_pixel = (r , g , b)
    encoded.append(new_pixel)
    
msg = []
for bit in encoded:
    rr , gg , bb = bit
    msg.append(rr)
    msg.append(gg)
    msg.append(bb)
    i = len(msg)
    if msg[(i-8) : i] == [1, 1, 1 , 1 ,1 , 1, 1, 1]:
        break
print(msg)
print(len(msg))

msg_bits = []
i = 0
while i < len(msg):
    msg_bit = msg[i : i+8]
    msg_bits.append(msg_bit)
    i+=8

word = ""
for msg_bit in msg_bits:
    letter_bit = ""
    for m in msg_bit:
        letter_bit += str(m)
    letter = chr(int(letter_bit , 2))
    word+= letter

print(word)



        


    





    
            







