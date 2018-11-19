try:
    from PIL import Image
except ImportError:
    import Image
import getopt, sys, pytesseract

# default parameters
tesseract_path = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
language = 'pol'
image_path = 'test/test-file.jpg'
result_file_name = 'test/output.txt'

# get parameters
try:
    opts, args = getopt.getopt(sys.argv[1:], "i:o:l:", ["image-path=", "output-file=", "lang="])
except getopt.GetoptError:
    print("Invalid parameters.")
    sys.exit(2)

for opt, arg in opts:
    if opt in ("-i", "--image-path"):
        image_path = arg
    elif opt in ("-o", "--output-file"):
        result_file_name = arg
    elif opt in ("-l", "--lang"):
        language = arg

# Setup tesseract
pytesseract.pytesseract.tesseract_cmd = tesseract_path

# Check extension
# print("Checking extension...")

# Convert to image
# print("Converting to image file...")

# Save text to file
print("Extracting text from image...")
with open(result_file_name, 'w', encoding='utf-16') as output_file:
    output_file.write(pytesseract.image_to_string(Image.open(image_path), lang=language))

print("Text extracted successfully!")