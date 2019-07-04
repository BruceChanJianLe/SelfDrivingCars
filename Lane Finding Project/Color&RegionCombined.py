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
left_bottom_down = [0, 539]
right_bottom_down = [959, 539]
right_bottom_up = [959, 399]
left_bottom_up = [0, 399]
apex = [479, 327]

# Creating a mask with white pixel
mask = np.zeros(img.shape, dtype=np.uint8)

# Points to be cropped
roi_corners = np.array([[left_bottom_down, right_bottom_down, apex]], dtype=np.int32)

# Fill the ROI into the mask
cv2.fillPoly(mask, roi_corners, color=[255, 255, 255])

# Applying the mask to the image
masked_image = cv2.bitwise_and(img_copy, mask)

# Set the color threshold for the image
R_threshold = 200
G_threshold = 200
B_threshold = 200
RGB_threshold = [R_threshold, G_threshold, B_threshold]

# Detect the pixel below the threshold
thresholds = (masked_image[:, :, 0] < RGB_threshold[0]) | (masked_image[:, :, 1] < RGB_threshold[1]) | (masked_image[:, :, 2] < RGB_threshold[2])
masked_image[thresholds] = [0, 0, 0]

# Change color from white to red
masked_image[~thresholds] = [0, 0, 255]

# Show only the detected red lines in ROI
cv2.imshow('Lanes_Detected', masked_image)

# Show on top of the original image
img_copy[~thresholds] = [0, 0, 255]

cv2.imshow('Original_with_Lanes_Detected', img_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()
