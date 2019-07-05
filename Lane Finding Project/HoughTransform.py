import cv2
import numpy as np


# Load the image
img = cv2.imread('exit-ramp.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Guassian Blur
kernel_size = (5, 5)
blur_gray = cv2.GaussianBlur(img, kernel_size, 0)

# CannyEdge
edges = cv2.Canny(blur_gray, threshold1=25, threshold2=200)

# Masking
mask = np.zeros_like(edges)     # Note that the input is only edges, without .shape
ignore_mask_color = 255
vertices = np.array([[(48, 537), (926, 536), (520, 282), (436, 273)]], dtype=np.int32)
cv2.fillPoly(mask, vertices, ignore_mask_color)

# Bitwise_and only work when 2 sources are the same type and size
masked_edges = cv2.bitwise_and(mask, edges)

# Hough Transformation
rho = 2
theta = np.pi / 180
threshold = 15
min_line_length = 45
max_line_gap = 15
# Make a same size blank image to draw lines
line_image = img.copy() * 0

# Detect the lines using Hough Lines
lines = cv2.HoughLinesP(masked_edges, rho,
                        theta, threshold, np.array([]), min_line_length, max_line_gap)

# Iterate over the output lines and draw lines on the blank image
for line in lines:
    for x1, y1, x2, y2 in line:
        cv2.line(line_image, (x1, y1), (x2, y2), [0, 0, 255], 10)

# Overlap the two images
combined_img = cv2.addWeighted(img, 0.8, line_image, 1, 0)

# Display the combined image
cv2.imshow('Lanes_Found_Image', combined_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
