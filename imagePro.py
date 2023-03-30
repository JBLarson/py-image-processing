#!/usr/bin/python3

import cv2
from time import sleep


# Read the image
image = cv2.imread('starryNight.jpg')

cv2.imshow('Original Image', image)
sleep(2)


# 1. Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image', gray_image)
sleep(5)
cv2.imwrite('starryNight_gray.jpg', gray_image)

# 2. Apply Gaussian blur
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
cv2.imwrite('starryNight_blurred.jpg', blurred_image)

# 3. Detect edges using Canny edge detection
edges_image = cv2.Canny(gray_image, 100, 200)
cv2.imwrite('starryNight_edges.jpg', edges_image)

# Display the processed images (optional)

cv2.imshow('Grayscale Image', gray_image)
sleep(2)
cv2.imshow('Blurred Image', blurred_image)
sleep(2)
cv2.imshow('Edges Image', edges_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
