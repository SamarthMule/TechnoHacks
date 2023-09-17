from tkinter import *

root = Tk()
root.title('Temperature Converter')
root.geometry()
root.config(bg='plum')
root.resizable(False, False)

my_frame = Frame(root,background='plum')
my_frame.pack(padx=5,pady=5)

Options = ["Fahrenheit","Celsius","Kelvin"]

temp1 = Entry(my_frame,font=("Helvetica",19),width=10,justify=CENTER)
temp1.grid(row=0,column=0,padx=5,pady=5)

clicked1 = StringVar()
clicked1.set("Fahrenheit")
drop1 = OptionMenu(my_frame,clicked1,*Options)
drop1.config(font=("Helvetica",15),bg="lightblue",width=10)
drop1.grid(row=0,column=1,padx=5,pady=5)

temp2 = Label(my_frame,font=("Helvetica",19),width=9,text="--------")
temp2.grid(row=1,column=0,padx=5,pady=5)

clicked2 = StringVar()
clicked2.set("Celsius")
drop1 = OptionMenu(my_frame,clicked2,*Options)
drop1.config(font=("Helvetica",15),bg="lightblue",width=10)
drop1.grid(row=1,column=1,padx=5,pady=5)

def convert():
    f = clicked1.get()
    t = clicked2.get()
    ini = int(temp1.get())
    if f == t:
        temp2.config(text=ini)
        return
    if f == "Fahrenheit":
        if t == "Celsius":
            ans = round((ini - 32)*(5/9),2)
            temp2.config(text=ans)
        else:
            ans = round((ini - 32)*(5/9) + 273.15,2)
            temp2.config(text=ans)
    elif f == "Celsius":
        if t == "Fahrenheit":
            ans = round((ini*(9/5)) + 32,2)
            temp2.config(text=ans)
        else:
            ans = round(ini + 273.15,2)
            temp2.config(text=ans)
    else:
        if t == "Celsius":
            ans = round(ini - 273.15,2)
            temp2.config(text=ans)
        else:
            ans = round((ini - 273.15)*(9/5) + 32,2)
            temp2.config(text=ans)
    

button = Button(root,text="Convert",command=convert,font=("Helvetica",15),
                bg="lavender",fg="purple",activebackground="purple",activeforeground="plum"
                )
button.pack(padx=5,pady=10)

root.mainloop()