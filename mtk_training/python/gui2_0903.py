from tkinter import *
from jieba.analyse import extract_tags
import time
import threading

class MyFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.l1 = Label(self, text="輸入新聞")
        self.l1.pack()
        self.t1 = Text(self, height=10)
        self.t1.pack()
        self.b1 = Button(self,
                         text="分析",
                         command=self.analyse_thread,
                         bg="orange")
        self.b1.pack(pady=20,
                     expand=True,
                     fill=BOTH)
        self.result = Label(self, text="按上面得到關鍵詞")
        self.result.pack()

    def analyse_thread(self):
        t = threading.Thread(target=self.analyse)
        t.start()

    def analyse(self):
        time.sleep(5)
        news = self.t1.get("1.0", "end")
        keywords = extract_tags(news, 5)
        self.result["text"] = str(keywords)

# 1. 元件(父元件) 2. 元件.排版(pack grid)
window = Tk()
window.geometry("500x500+200+200")


f1 = MyFrame(window)
f1.pack(padx=20, pady=20)

window.mainloop()