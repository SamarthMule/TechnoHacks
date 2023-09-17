from tkinter import *
import random

root = Tk()
root.title('Password Generator')
root.geometry("500x200")
root.config(bg='lavender')
root.resizable(False, False)

def play():
    ch = x.get()
    comp = random.randint(0,2)
    Comp_ch.config(text=choice[comp])
    if ch == comp:
        Winner.config(text="Draw")
        return
    if ch == 0:
        if comp == 1:
            Winner.config(text="Computer Wins")
        if comp == 2:
            Winner.config(text="You Wins")
    if ch == 1:
        if comp == 2:
            Winner.config(text="Computer Wins")
        if comp == 0:
            Winner.config(text="You Wins")
    if ch == 2:
        if comp == 0:
            Winner.config(text="Computer Wins")
        if comp == 1:
            Winner.config(text="You Wins")
    

choice = ["Rock","Paper","Scissor"]
x = IntVar()
my_frame = Frame(root,background='plum')
my_frame.pack(padx=5,pady=5)
for i in range(len(choice)):
    radio_button = Radiobutton(my_frame,text=choice[i],
                               variable=x,value=i,
                               font=("Times",20),
                               command=play,width=5,
                               padx=10,pady=10,justify=CENTER)
    radio_button.grid(row=0,column=i,padx=16,pady=15)
Comp_ch = Label(root,width=20,font=("Times",20),text="Select Any One")
Comp_ch.pack(padx=5,pady=5)
Winner = Label(root,width=20,font=("Times",20),text="Winner Name")
Winner.pack(padx=5,pady=5)

root.mainloop()