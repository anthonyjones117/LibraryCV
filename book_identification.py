import cv2
import pytesseract
from matplotlib import pyplot as plt
image_path = "images/books.jpg"
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print("Grayscale Image:")
plt.imshow(gray)
plt.figure(figsize=(10, 6))
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")
plt.show()
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
extracted_text = pytesseract.image_to_string(gray)
print(" Extracted Text:\n")
print(extracted_text)
data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)

n_boxes = len(data['level'])
for i in range(n_boxes):
    (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
    cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 0, 0), 2)

plt.figure(figsize=(10, 6))
plt.imshow(gray)
plt.title("Image with Text Bounding Boxes")
plt.axis("off")
plt.show()