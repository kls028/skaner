import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def scan_document(image_path):
   # Wczytaj obraz z pliku
   image = cv2.imread(image_path)

   # Konwertuj obraz na skalę szarości
   gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

   # Zastosuj progowanie do wyodrębnienia tekstu na obrazie
   thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

   # Wykonaj OCR na obrazie za pomocą biblioteki pytesseract
   text = pytesseract.image_to_string(thresh, lang='eng',
                                       config='--psm 11')


   return str(text)

lines = scan_document("zdj/testt.jpg")
with open('text.txt', 'w') as f:
    f.write(lines)



