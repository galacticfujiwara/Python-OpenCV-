from PIL import Image
import pytesseract
import argparse
import cv2
import os
from googletrans import Translator
from tkinter import filedialog
file_path = filedialog.askopenfilename()
trans=Translator()

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'


resim = cv2.imread(file_path)
gray = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

dosya_Adi = "{}.png".format(os.getpid())
cv2.imwrite(dosya_Adi, gray)
metin = pytesseract.image_to_string(Image.open(dosya_Adi))
translated=trans.translate(metin,dest='tr')
os.remove(dosya_Adi)
print("Orjinal: ",metin)
print("Türkce Hali: ",translated.text)

cv2.waitKey(0)
cv2.destroyAllWindows()