
from paddleocr import PaddleOCR

ocr = PaddleOCR(
    use_textline_orientation=True,
    lang="en"
)

result = ocr.predict("sample1.png")

print(result)
