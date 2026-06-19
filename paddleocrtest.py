from paddleocr import PaddleOCR

ocr = PaddleOCR(lang="en")

result = ocr.predict("image.png")

for page in result:
    print(page["rec_texts"])