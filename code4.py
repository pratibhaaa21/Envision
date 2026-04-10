word = "SECRET"
new = ""
for p in word:
    new+= format(ord(p), '0b') + " "
print(new)    


