import cv2
import numpy as np


# Load the image
img = cv2.imread('Finding_White_Color.jpg')

# Print the associated information in the loaded image
print(f'This image is of type: {type(img)}, with dimension of: {img.shape}')

# Obtain the size of the image
img_height = img.shape[0]
img_width = img.shape[1]

# Make a deep copy of the image
img_copy = img.copy()

# Define a triangular region of interest
# Noting that the origin (x=0, y=0) is at the top left corner of the image
left_bottom = [0, 539]
right_bottom = [900, 300]
apex = [400, 0]


