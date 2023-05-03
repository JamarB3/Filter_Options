#Import matplotlib -> Image Processing
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import random


#Adds red stripes that run horizontally on the image
#For red stripes, r value = 255
def red_stripes(image_matrix):
    for row in range(len(image_matrix)):
      if (row // 50) % 2 == 0:
        for col in range(len(image_matrix[row])):
          image_matrix[row][col][0] = 1.0
          #1.0 = 255
                
    return image_matrix
                  
#Gradually darkens the given image
def fade_to_black(image_matrix):
    #Dimensions of the image
    height, width, channels = image_matrix.shape
    for row in range(height):
      for col in range(width):
        for ch in range(channels):
          image_matrix[row][col][ch] *= (col / width)
                
    return image_matrix

#
def hyper_wave(image_matrix):
  #Dimensions of the image
  height, width, channels = image_matrix.shape
  for row in range(height):
    for col in range(width):
      for ch in range(channels):
        image_matrix[row][col][ch] **= (col / width)
                
  return image_matrix
#Darkens all pixels except for red values
def red_distortion (image_matrix):
  height, width, channels = image_matrix.shape
  for row in range(height):
    for col in range(width):
      for ch in range(channels):
        image_matrix[row][col][ch] **= (col * width)
        
  return image_matrix

#Function returns a copy of the image with inverted colors
def color_inversion(photo):
  #Dimensions of the image
  height, width, channels = photo.shape
  #Since image is a read-only -> create copy
  copy_image = photo.copy()
  #Iterates over each pixel within the image
  for row in range(height):
    for col in range(width):
      for chl in range(channels):
        #Every pixel/channel -> Subtract 1 to "flip" the values
        copy_image[row][col][chl] = 1 - copy_image[row][col][chl]
  #Returns the inverted version
  return copy_image

# Read the image file
img = mpimg.imread("valstrax.png")

#Apply the filter
filtered_img = red_stripes(img)

# Display the filtered image using Matplotlib
plt.imshow(filtered_img)
plt.show()