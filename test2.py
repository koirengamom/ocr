from paddleocr import PaddleOCR

ocr = PaddleOCR(
    lang="en",
    device="cpu",
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False
)

result = ocr.predict("image.png")

for page in result:
    print(page["rec_texts"])