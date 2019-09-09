from PIL import ImageColor

(r, g, b) = ImageColor.getcolor("#0000ff", "RGB")
print(r,g,b)
(r, g, b) = ImageColor.getcolor("rgb(0,0,255)", "RGB")
print(r,g,b)
(r, g, b) = ImageColor.getcolor("Blue", "RGB")
print(r,g,b)
(r, g, b, a) = ImageColor.getcolor("#0000ff", "RGBA")
print(r,g,b,a)
(r, g, b, a) = ImageColor.getcolor("rgb(0,0,255)", "RGBA")
print(r,g,b,a)
(r, g, b, a) = ImageColor.getcolor("Blue", "RGBA")
print(r,g,b,a)
