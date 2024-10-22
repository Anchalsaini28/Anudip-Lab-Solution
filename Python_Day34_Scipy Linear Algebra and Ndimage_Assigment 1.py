# Lab1: Using a Sobel filter, filter the image and then display it.
# Input: https://github.com/AnudipAE/DANLC/blob/master/dog.jpg

# Import necessary libraries
import numpy as np  # For numerical operations and handling arrays
import matplotlib.pyplot as plt  # For displaying images and plotting
from scipy import ndimage  # For applying image processing functions like Sobel filter
import imageio  # For reading and writing image files (similar to OpenCV or PIL)

# Load an example image
# The image file 'dog.jpg' is read using imageio.imread(), which loads it as a numpy array
# You need to replace 'dog.jpg' with the actual path of your image.
image = imageio.imread('dog.jpg')  # Replace with your image file path

# Apply the Sobel filter on the image
# ndimage.sobel() applies the Sobel filter to the image. It computes the gradient,
# highlighting the edges. By default, this calculates for both X and Y directions.
sobel_filtered_image = ndimage.sobel(image)

# Plot the original image
plt.figure(figsize=(6, 6))  # Create a figure window with a specific size
plt.imshow(image, cmap='gray')  # Display the original image in grayscale
plt.title('Original Image')  # Set the title for the image plot
plt.axis('off')  # Turn off axis labels and ticks
plt.show()  # Display the image

# Plot the Sobel filtered image
plt.figure(figsize=(6, 6))  # Create another figure window with the same size
plt.imshow(sobel_filtered_image, cmap='gray')  # Display the Sobel filtered image
plt.title('Sobel Filtered Image')  # Set the title for the filtered image
plt.axis('off')  # Turn off axis labels and ticks
plt.show()  # Display the filtered image
