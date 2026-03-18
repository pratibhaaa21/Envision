pixels = [150, 151, 152, 153, 154, 155, 156, 157]
secret_bits = [1, 0, 1, 1, 0, 0, 1, 0]

new = []
def embed_bit(pixels , secret_bits):
        return (pixels & ~1) | secret_bits

for p , s in zip( pixels , secret_bits):      
        save = embed_bit(p , s)
        new.append(save)
print(new)        


# if bit is 0 , then odd will change to even , and even will remain even.
# if but is 1 , then even will change to odd and odd will remain odd .
        
    
        