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

# Set the color threshold for the image
R_threshold = 200
G_threshold = 200
B_threshold = 200
RGB_threshold = [R_threshold, G_threshold, B_threshold]

# Detect the pixel below the threshold
thresholds = (img[:, :, 0] < RGB_threshold[0]) | (img[:, :, 1] < RGB_threshold[1]) | (img[:, :, 2] < RGB_threshold[2])
img_copy[thresholds] = [0, 0, 0]

# Show the original img with the thresholded one
cv2.imshow('Original_and_Threshold', np.hstack([img, img_copy]))

cv2.waitKey(0)
cv2.destroyAllWindows()
