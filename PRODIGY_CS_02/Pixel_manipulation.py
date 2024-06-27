from PIL import Image # type: ignore


def encrypt_image(image_path, output_path, key):

    img = Image.open(image_path)
    width, height = img.size
    
    
    key_int = [ord(char) for char in key]
    key_length = len(key_int)
    

    pixels = img.load()
    

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            r = r ^ key_int[(x + y) % key_length]
            g = g ^ key_int[(x + y) % key_length]
            b = b ^ key_int[(x + y) % key_length]
            pixels[x, y] = (r, g, b)
    
  
    img.save(output_path)


def decrypt_image(image_path, output_path, key):
    encrypt_image(image_path, output_path, key)  

# Main 
def main():
    print("Simple Image Encryption Tool")


    image_path = input("Enter the path to the image file: ")
    output_path = input("Enter the output path for the encrypted/decrypted image: ")
    key = input("Enter the encryption/decryption key (a string): ")


    encrypt_image(image_path, output_path, key)
    print(f"Image encrypted and saved to {output_path}")

   
    decrypted_path = input("Enter the output path for the decrypted image: ")
    decrypt_image(output_path, decrypted_path, key)
    print(f"Image decrypted and saved to {decrypted_path}")

if __name__ == "__main__":
    main()
