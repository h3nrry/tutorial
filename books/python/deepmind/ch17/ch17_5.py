#ch17_5.py
from PIL import Image

rushMore = Image.open("rushmore.jpeg")  #建立Pillow
print("列出物件福檔名： ", rushMore.format)
print("列出物件單數：", rushMore.format_description)