from tkinter import *
import random
import string
root = Tk()
root.title('Password Generator')
root.geometry("500x200")
root.config(bg='lavender')
root.resizable(False, False)

def Generator():
    op = clicked.get()
    if op == "Simple Password":
        CharacterList = string.digits + string.ascii_letters + "~!@#$%^&*()-+=<>?"
        password = ""
        for i in range(6):
            letter= random.choice(CharacterList)
            password += letter
        label.config(text=password)
    if op == "Digits Only":
        password = ""
        for i in range(6):
            letter= random.choice(string.digits)
            password += letter
        label.config(text=password)
    if op == "Letters Only":
        password = ""
        for i in range(6):
            letter= random.choice(string.ascii_letters)
            password += letter
        label.config(text=password)
    if op == "Symbols Only":
        password = ""
        for i in range(6):
            letter= random.choice("~!@#$%^&*()-+=<>?")
            password += letter
        label.config(text=password)
    if op == "Strong Password":
        CharacterList = string.digits + string.ascii_letters + "~!@#$%^&*()-+=<>?"
        password = ""
        for i in range(2):
            letter= random.choice(string.digits) + random.choice(string.ascii_letters) + random.choice("~!@#$%^&*()-+=<>?")
            password += letter
        label.config(text=password)

label = Label(root,font=("Times",25),width=15,text="Password")
label.pack(padx=10,pady=20)

Options = ["Simple Password","Digits Only","Letters Only","Symbols Only","Strong Password"]
clicked = StringVar()
clicked.set("Simple Password")
Options = OptionMenu(root,clicked,*Options)
Options.config(font=("Time",19),width=15,bg="plum")
Options.pack()

button = Button(root,font=("Time",19),width=16,text="Generate" , command=Generator)
button.pack(padx=10,pady=20)

root.mainloop()