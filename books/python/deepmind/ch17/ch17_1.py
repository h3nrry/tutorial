#ch17_1.py

#Import PIL can be used pip install Pillow
from PIL import ImageColor

print(ImageColor.getrgb("#0000ff"))
print(ImageColor.getrgb("rgb(0,  0,255)"))
print(ImageColor.getrgb("rgb(0%,0%,100%)"))
print(ImageColor.getrgb("Blue"))
print(ImageColor.getrgb("blue"))

(r1, g1, b1) = ImageColor.getrgb("#0000ff")
(r2, g2, b2) = ImageColor.getrgb("rgb(0,  0,255)")
(r3, g3, b3) = ImageColor.getrgb("rgb(0%,0%,100%)")
(r4, g4, b4) = ImageColor.getrgb("Blue")
(r5, g5, b5) = ImageColor.getrgb("blue")

print(r1, g1, b1)
print(r2, g2, b2)
print(r3, g3, b3)
print(r4, g4, b4)
print(r5, g5, b5)
