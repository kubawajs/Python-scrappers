try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# TODO: image name as parameter
# TODO: language as parameter
# TODO: add to readme info about tesseract-ocr installation

# Consts
tesseract_path = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
language = 'pol'

# Setup tesseract
pytesseract.pytesseract.tesseract_cmd = tesseract_path

# Check extension
# print("Checking extension...")

# Convert to image
# print("Converting to image file...")

# Text image to string
print("Extracting text from image...")
print(pytesseract.image_to_string(Image.open('test/test-file.jpg'), lang=language))

# get a searchable PDF
pdf = pytesseract.image_to_pdf_or_hocr('test/test-file.jpg', extension='pdf')

# End
print("Text extracted successfully!")