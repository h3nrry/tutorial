from tkinter import *

def cal():
    global e1
    global l2
    try:
        f = float(e1.get())
        l2["text"] = round(f)
    except ValueError:
        l2["text"] = "不要再亂輸入了!!!"

# 1. 元件(父元件) 2. 元件.排版(pack grid)
window = Tk()
window.geometry("500x500+200+200")

f1 = Frame(window)
f1.pack()

l1 = Label(f1, text="輸入小數")
l1.pack()
e1 = Entry(f1)
e1.pack()
b1 = Button(f1, text="四捨五入", command=cal)
b1.pack()
l2 = Label(f1, text="按上面按鈕得到結果")
l2.pack()

window.mainloop()