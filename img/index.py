# 图片文字识别
from PIL import Image
# 导入图片识别库
import pytesseract

text = pytesseract.image_to_string(Image.open('testimage.png'), lang='chi_sim', config="-psm 6")
print(text)