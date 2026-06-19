from paddleocr import PaddleOCR
import os

# Initialize OCR model
ocr = PaddleOCR(
    lang="en",
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False,
    device="cpu"
)

# Input image path
image_path = input("Enter image path: ")

# Check if file exists
if not os.path.exists(image_path):
    print("Error: Image file not found!")
    exit()

print("\nProcessing image...\n")

# Perform OCR
result = ocr.predict(image_path)

# Output text file
output_file = "output.txt"

with open(output_file, "w", encoding="utf-8") as f:

    for page in result:

        texts = page["rec_texts"]
        scores = page["rec_scores"]

        print("Detected Text:\n")

        for text, score in zip(texts, scores):

            print(f"Text       : {text}")
            print(f"Confidence : {score:.4f}")
            print("-" * 50)

            f.write(text + "\n")

print(f"\nOCR completed successfully.")
print(f"Extracted text saved to: {output_file}")