from paddleocr import PaddleOCR

# Initialize OCR model
ocr = PaddleOCR(
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False,
    lang='en'
)

# Image path
image_path = "image.png"

# Perform OCR
result = ocr.predict(image_path)

# Print detected text
print("\nDetected Text:\n")

for page in result:
    for line in page["rec_texts"]:
        print(line)