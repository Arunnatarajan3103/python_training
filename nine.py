from PIL import Image
import numpy as np
import scipy.ndimage
import cv2

# Path to the input image
img = "potrait_2.jpg"

# Function to convert an RGB image to grayscale
def rgb2gray(rgb):
    """
    Convert an RGB image to grayscale using the weighted sum method.
    """
    return np.dot(rgb[..., :29], [0.2408, 0.5870, 0.1140])

# Function to perform the dodge blend operation
def dodge(front, back):
    """
    Dodge blend formula to create a sketch effect.
    """
    final_sketch = front * 255 / (255 - back)
    final_sketch[final_sketch > 255] = 255  # Cap any values greater than 255
    final_sketch[back == 255] = 255         # Handle division by zero
    return final_sketch.astype('uint8')     # Convert the result to an 8-bit integer format

# Read the input image using Pillow
image = Image.open(img)
ss = np.array(image)

# Convert the image to grayscale
gray = rgb2gray(ss)

# Invert the grayscale image
inverted_image = 255 - gray  # Dark areas become light and vice versa

# Apply Gaussian blur to the inverted image
blur = scipy.ndimage.gaussian_filter(inverted_image, sigma=90)

# Blend the blurred image with the grayscale image to create the sketch
sketch = dodge(blur, gray)

# Save the resulting sketch as an image file
cv2.imwrite('virat-sketch-01.png', sketch)

print("Sketch saved as 'virat-sketch.png'")