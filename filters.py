import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


#For red stripes, r value = 255

  
def red_stripes(image_matrix):
    for row in range(len(image_matrix)):
      if (row // 50) % 2 == 0:
        for col in range(len(image_matrix[row])):
          image_matrix[row][col][0] = 1.0
          #1.0 = 255
                
    return image_matrix
            

            
    
    
    
    
#Grayscale value: All RGB must be the same.

def fade_to_black(image_matrix):
    height, width, channels = image_matrix.shape
    
    for row in range(height):
      for col in range(width):
        for ch in range(channels):
          image_matrix[row][col][ch] *= (col / width)
                
    return image_matrix


def hyper_wave(image_matrix):
  height, width, channels = image_matrix.shape
  for row in range(height):
    for col in range(width):
      for ch in range(channels):
        image_matrix[row][col][ch] **= (col / width)
                
  return image_matrix
  


# Read the image file
img = mpimg.imread("valstrax.png")

# Apply the red_stripes filter
filtered_img = hyper_wave(img)

# Display the filtered image using Matplotlib
plt.imshow(filtered_img)
plt.show()