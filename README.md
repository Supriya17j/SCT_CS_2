# SCT_CS_2

# Task 02 – Image Encryption using Python

## Description
This project demonstrates a simple image encryption and decryption technique
using pixel manipulation. Each pixel's RGB values are modified using a numeric key.

## How it Works
- Encryption: (pixel_value + key) % 256
- Decryption: (pixel_value - key) % 256

## Tools Used
- Python
- Pillow (PIL)

## How to Run
1. Place an image named `input.png` in the folder
2. Run the program
3. Enter a key between 0–255
4. Encrypted and decrypted images will be generated

## Output
- encrypted.png
- decrypted.png
