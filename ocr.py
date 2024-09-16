from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import cv2
import numpy as np

# Convert PDF to list of images (one image per page)
images = convert_from_path(r"C:\Users\chaitu\Downloads\2CN4BN.pdf")


# Configure tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Perform OCR on the first image (example for one page)
image = images[0]
data = pytesseract.image_to_boxes(image)  # returns string containing box information

# Convert PIL Image to OpenCV format
image_cv = np.array(image)
image_cv = cv2.cvtColor(image_cv, cv2.COLOR_RGB2BGR)

h, w, _ = image_cv.shape  # get image dimensions
print(image_cv.shape)
# Draw bounding boxes on the image
for box in data.splitlines():
    b = box.split(' ')
    x1, y1, x2, y2 = int(b[1]), h - int(b[2]), int(b[3]), h - int(b[4])
    cv2.rectangle(image_cv, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imwrite('output_with_bounding_boxes.png', image_cv)


import os

print(os.getcwd())


