# OCR CLI with PaddlePaddle

This repository provides a small Python command-line application for extracting text from:

- image files such as `.jpg`, `.jpeg`, `.png`, `.bmp`, `.tif`, `.tiff`, and `.webp`
- scanned PDF documents by rendering each page and running OCR on the resulting images

It uses PaddlePaddle as the runtime and PaddleOCR for the OCR pipeline, then saves the extracted text into a `.txt` file.

## Features

- Command-line interface
- OCR for images and scanned PDFs using PaddlePaddle-backed inference
- Screen output for extracted text
- Text file export
- Basic evaluation metrics for speed, confidence, and optional reference-text accuracy

## Install

```bash
pip install -r requirements.txt
```

If you want GPU acceleration, install a PaddlePaddle build that matches your CUDA environment.

## Usage

Process a single image:

```bash
python main.py sample.jpg
```

Process a scanned PDF:

```bash
python main.py document.pdf
```

Process multiple files or a directory:

```bash
python main.py ./inputs -o extracted_text.txt
```

Optional evaluation against a plain-text ground truth file:

```bash
python main.py sample.jpg --reference reference.txt
```

## Output

The application prints the extracted text, processing time, average OCR confidence, and optional character-level accuracy estimates. It also writes the combined extracted text to:

- the file passed with `--output`
- the input file name with a `.txt` suffix when a single file is processed
- `ocr_output.txt` in the current directory when multiple inputs are processed and no output path is given

## Notes

- PDF OCR is done by rasterizing pages with PyMuPDF, which works well for scanned PDFs.
- This is a reusable starter app, so you can extend it with JSON output, batch reporting, or API packaging later.