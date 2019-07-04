import cv2


# Load the image
img = cv2.imread('exit-ramp.jpg')

# Covert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Guassian Blur, note that it always take a odd number
kernel_size = 3
blur_gray = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)

# CannyEdge
low_threshold = 25
high_threshold = 200
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

# Display the image
cv2.imshow('CannyEdge', edges)

# Close the windows properly
cv2.waitKey(0)
cv2.destroyAllWindows()
