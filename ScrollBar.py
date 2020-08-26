from tkinter import *
top = Tk()
top.geometry("250x250")
top.title("My scrollbar")

sb = Scrollbar(top)
sb.pack(side = RIGHT, fill = Y)
myList = Listbox(top,yscrollcommand = sb.set)

for line in range(30):
    myList.insert(END,"Number" + str(line))
myList.pack(side = LEFT)
sb.config(command = myList.yview)
mainloop()