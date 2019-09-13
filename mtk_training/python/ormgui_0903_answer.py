from tkinter import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models_0903 import Student, Phone
import os

class MyFrame(Frame):
    def __init__(self, master, engine):
        Frame.__init__(self, master)
        self.l1 = Label(text="輸入姓名")
        self.l1.pack()
        self.e1 = Entry()
        self.e1.pack()
        self.b1 = Button(text="查詢", command=self.query_phone)
        self.b1.pack()
        self.result = Label(text="按上面查詢")
        self.result.pack()
        S = sessionmaker(bind=engine)
        self.session = S()

    def query_phone(self):
        result = ""
        q = (self.session
                 .query(Student)
                 .filter_by(name=self.e1.get()))
        student = q.first()
        for p in student.phones:
            result = result + str(p) + "\n"
        self.result["text"] = result

window = Tk()
window.geometry("500x500")
dn = os.path.dirname(__file__)
fn = "sqlite:///" + os.path.join(dn, "data_0903.sqlite")
engine = create_engine(fn, echo=False)

f1 = MyFrame(window, engine)
f1.pack()
window.mainloop()