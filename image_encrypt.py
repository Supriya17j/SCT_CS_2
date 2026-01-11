from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    img.save("encrypted.png")
    print("Image encrypted successfully.")


def decrypt_image(image_path, key):
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    img.save("decrypted.png")
    print("Image decrypted successfully.")


key = int(input("Enter encryption key (0-255): "))

encrypt_image("input.png", key)
decrypt_image("encrypted.png", key)
