from pdf2image import convert_from_path
import easyocr
import cv2
import numpy as np

# Step 1: Convert PDF to list of images
images = convert_from_path(r"C:\Users\chaitu\Downloads\Internship Letter_Chaitaanya Deepak Naidu (1).pdf")

# Step 2: Initialize the EasyOCR reader
reader = easyocr.Reader(['en'], gpu=False)  # You can enable GPU by setting gpu=True if available

# Check if images were successfully converted
if images:
    # Step 3: Perform OCR on the first image
    image = np.array(images[0])  # Convert PIL image to numpy array
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # Convert RGB to BGR for OpenCV compatibility
    result = reader.readtext(image)

    # Step 4: Draw bounding boxes on the image
    for detection in result:
        bbox, text, confidence = detection
        # Get bounding box coordinates
        top_left = tuple([int(val) for val in bbox[0]])
        bottom_right = tuple([int(val) for val in bbox[2]])

        # Draw rectangle around detected text
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

        # Optionally, annotate the image with detected text
        cv2.putText(image, text, top_left, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    # Save or display the output image
    output_path = 'output_with_easyocr_boxes.png'
    cv2.imwrite(output_path, image)


    print(f"Image saved at {output_path}")
else:
    print("No images found in the PDF file!")