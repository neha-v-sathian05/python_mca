
import numpy as np

# Create an image matrix using pixel values
image = np.array([
    [50, 100, 150],
    [200, 100, 50],
    [75, 125, 175]
])

# Display the original image matrix
print("Original Image Matrix:")
print(image)

# Reshape the image matrix
reshaped_image = image.reshape(1, 9)
print("\nReshaped Image Matrix:")
print(reshaped_image)

# Slice a region of the image
region = image[0:2, 0:2]
print("\nSliced Image Region:")
print(region)

# Adjust brightness using broadcasting and clip()
bright_image = np.clip(image + 50, 0, 255)
print("\nImage After Brightness Adjustment:")
print(bright_image)

# Perform matrix multiplication using np.dot()
transform = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

result = np.dot(image, transform)
print("\nResult After Matrix Multiplication:")
print(result)
