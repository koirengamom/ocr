from paddleocr import PaddleOCR
from pdf2image import convert_from_path
import os

# Initialize OCR
ocr = PaddleOCR(
    lang="en",
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False,
    device="cpu"
)

file_path = input("Enter image or PDF path: ")

if not os.path.exists(file_path):
    print("Error: File not found!")
    exit()

all_text = []

# ---------- PDF OCR ----------
if file_path.lower().endswith(".pdf"):

    print("\nProcessing PDF...\n")

    pages = convert_from_path(file_path)

    for page_num, page in enumerate(pages, start=1):

        image_name = f"page_{page_num}.png"
        page.save(image_name, "PNG")

        result = ocr.predict(image_name)

        all_text.append(f"\n===== PAGE {page_num} =====\n")

        for page_result in result:
            for text in page_result["rec_texts"]:
                print(text)
                all_text.append(text)

# ---------- IMAGE OCR ----------
else:

    print("\nProcessing Image...\n")

    result = ocr.predict(file_path)

    for page_result in result:
        for text in page_result["rec_texts"]:
            print(text)
            all_text.append(text)

# Save Output
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(all_text))

print("\nOCR Completed Successfully!")
print("Output saved to output.txt")