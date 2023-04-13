from tkinter import *

class MyWindow:
    def __init__(self, win):

        self.lbl1 = Label(win, text = "Enter Given Name:")
        self.lbl1.place(x = 100, y = 50)

        self.lbl2 = Label(win,text = "Enter Middle Name:")
        self.lbl2.place(x=100,y=100)

        self.lbl3 = Label(win,text = "Enter Last Name:")
        self.lbl3.place(x=100,y=150)

        self.lbl3 = Label(win, text="My Full Name is:")
        self.lbl3.place(x=100, y=200)

        self.txt1 = Entry(win , bd = 1)
        self.txt1.place(x = 215, y = 50)

        self.txt2 = Entry(win, bd= 1)
        self.txt2.place(x = 215, y = 100)

        self.txt3 = Entry(win, bd = 3)
        self.txt3.place(x = 215, y = 150)

        self.txt4 = Entry(win, bd = 3)
        self.txt4.place(x = 215, y = 200)

        self.btnadd = Button(win, text = "Show Full Name:")
        self.btnadd.place(x = 200, y = 300)
        self.btnadd.bind('<Button-1>', self.add)


    def add(self, add):

        self.txt4.delete(0, 'end')
        num1 = str(self.txt1.get())
        num2 = str(self.txt2.get())
        num3 = str(self.txt3.get())
        result = num1 + num2 + num3
        self.txt4.insert(END, str(result))


window = Tk()
mywin = MyWindow(window)
window.geometry("600x400+10+10")
window.title("Full Name")
window.mainloop()