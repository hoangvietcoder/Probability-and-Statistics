from __future__ import print_function
import cv2 as cv
import argparse

# Load the source image
parser = argparse.ArgumentParser(description='Code for Histogram Equalization tutorial.')
parser.add_argument('--input', help='Path to input image.', default='Moon.jpg')
args = parser.parse_args()
src = cv.imread(cv.samples.findFile(args.input))
if src is None:
    print('Could not open or find the image:', args.input)
    exit(0)

# Convert it to grayscale
src = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

# Apply histogram equalization with the function cv::equalizeHist
dst = cv.equalizeHist(src)

# Display both images (original and equalized)
cv.imshow('Source image', src)
cv.imshow('Equalized Image', dst)

# Wait until user exists the program
cv.waitKey()
