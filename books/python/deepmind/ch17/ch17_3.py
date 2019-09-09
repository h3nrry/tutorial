from PIL import Image

rushMore = Image.open("rushmore.jpeg")   # 建立Pillow物件
print("列出物件聖態： ", type(rushMore))
width , height = rushMore.size
print("width: ", width)
print("height:", height)