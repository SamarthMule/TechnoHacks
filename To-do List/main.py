from tkinter import *
from tkinter import messagebox

tk = Tk()
tk.geometry()
tk.title('PythonGuides')
tk.config(bg='#223441')
tk.resizable(width=False, height=False)

fr = Frame(tk)
fr.pack(padx=10,pady=10)

lb = Listbox(fr,activestyle="none",width=25,font=("Times",20))
lb.pack(side=LEFT, fill=BOTH,padx=10,pady=10)

lst = []

for x in lst:
    lb.insert(END, x)

scr = Scrollbar(fr)
scr.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=scr.set)
scr.config(command=lb.yview)

entr = Entry(tk,font=("Times",20),width=25)
entr.pack(padx=10,pady=10)

def addbtnTSK():
    X = entr.get()
    if X != "":
        lb.insert(END, X)
        entr.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")


addbtn = Button(tk, text='Add Task', command=addbtnTSK,font=("Times",20))
addbtn.pack(fill=BOTH, expand=True, side=LEFT)

def delTSK():
    lb.delete(ANCHOR)

delbtn = Button(tk, text='Delete Task', command= delTSK,font=("Times",20))
delbtn.pack(fill=BOTH, expand=True, side=LEFT)

tk.mainloop()