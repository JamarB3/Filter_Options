from PIL import Image

# Open the image file
image = Image.open("Superfly Elite 2")

# Resize the image to fit in the terminal
max_width, max_height = 100, 100
image.thumbnail((max_width, max_height))

# Convert the image to ASCII characters
ascii_chars = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']
pixels = list(image.getdata())
ascii_pixels = [ascii_chars[int(sum(pixel) / 3 / 25.5)] for pixel in pixels]
ascii_image = ''.join(ascii_pixels)

# Print the ASCII image in the terminal
print(ascii_image)
