def embed_bit(pixel_value , secret_bit):
    return (pixel_value & ~1) | secret_bit  # changes the value of pixel_value to 0 anyway ,and returns secret_bit in every case . 

