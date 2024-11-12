from tkinter import *

def infort():
    label.config(text=info[var.get()])

root = Tk()
root.title("Телефоны")


info = {
    "Вася": "+7 9130782750",
    "Петя": "+4 9087654321",
    "Маша": "+7 8001234567"
}


var = StringVar()
var.set("Петя")

#Рамка
frame = Frame(root)
frame.pack(side=LEFT, padx=10, pady=10)


for name in info.keys():
    Radiobutton(frame, text=name, variable=var, value=name,
                indicatoron=0, command=infort, width=10, height=2).pack(fill=X, pady=2)


label = Label(root, text=info[var.get()], font=("Times New Roman", 14), anchor="center")
label.pack(padx=10, pady=10, expand=True, fill=BOTH)

root.mainloop()
