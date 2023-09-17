import tkinter

tk = tkinter.Tk()
tk.title("Calculator")
tk.config(bg="Green")
Total = ""


result = tkinter.Label(tk, text=" Result ",font=("Times",20),width=20)
result.grid(row=0, column=0, columnspan=4,padx=5,pady=5)

def add(X):
    global Total
    Total += X
    result.config(text=Total)

def clean():
    global Total
    Total = ""
    result.config(text=Total)

def final_Calc():
    global Total
    final_result = ""
    if Total != "":
        try:
            final_result = eval(Total)
        except:
            final_result = "error"
            Total = ""
    result.config(text=final_result)

btn1 = tkinter.Button(tk, text="1", command=lambda: add("1"),font=("Time",15),width=5,
                    bg="lightgreen",fg="darkgreen",activebackground="darkgreen",activeforeground="lightgreen")
btn1.grid(row=1, column=0,padx=5,pady=5)

btn2 = tkinter.Button(tk, text="2", command=lambda: add("2"),font=("Time",15),width=5,
                    bg="lightgreen",fg="darkgreen",activebackground="darkgreen",activeforeground="lightgreen")
btn2.grid(row=1, column=1,padx=5,pady=5)

btn3 = tkinter.Button(tk, text="3",  command=lambda: add("3"),font=("Time",15),width=5,
                    bg="lightgreen",fg="darkgreen",activebackground="darkgreen",activeforeground="lightgreen")
btn3.grid(row=1, column=2,padx=5,pady=5)

btnDiv = tkinter.Button(tk, text="/",  command=lambda: add("/"),font=("Time",15),width=5,
                    bg="lightgreen",fg="darkgreen",activebackground="darkgreen",activeforeground="lightgreen")
btnDiv.grid(row=1, column=3,padx=5,pady=5)

btn4 = tkinter.Button(tk, text="4",  command=lambda: add("4"),font=("Time",15),width=5,
                    bg="lightgreen",fg="darkgreen",activebackground="darkgreen",activeforeground="lightgreen")
btn4.grid(row=2, column=0,padx=5,pady=5)

btn5 = tkinter.Button(tk, text="5",  command=lambda: add("5"),font=("Time",15),width=5,
                    bg="lightgreen",fg="darkgreen",activebackground="darkgreen",activeforeground="lightgreen")
btn5.grid(row=2, column=1,padx=5,pady=5)

btn6 = tkinter.Button(tk, text="6",  command=lambda: add("6"),font=("Time",15),width=5,
                    bg="lightgreen",fg="darkgreen",activebackground="darkgreen",activeforeground="lightgreen")
btn6.grid(row=2, column=2,padx=5,pady=5)

btnmul = tkinter.Button(tk, text="*",  command=lambda: add("*"),font=("Time",15),width=5,
                    bg="lightgreen",fg="darkgreen",activebackground="darkgreen",activeforeground="lightgreen")
btnmul.grid(row=2, column=3,padx=5,pady=5)


btn7 = tkinter.Button(tk, text="7",  command=lambda: add("7"),font=("Time",15),width=5,
                    bg="lightgreen",fg="darkgreen",activebackground="darkgreen",activeforeground="lightgreen")
btn7.grid(row=3, column=0,padx=5,pady=5)

btn8 = tkinter.Button(tk, text="8",  command=lambda: add("8"),font=("Time",15),width=5,
                    bg="lightgreen",fg="darkgreen",activebackground="darkgreen",activeforeground="lightgreen")
btn8.grid(row=3, column=1,padx=5,pady=5)

btn9 = tkinter.Button(tk, text="9",  command=lambda: add("9"),font=("Time",15),width=5,
                    bg="lightgreen",fg="darkgreen",activebackground="darkgreen",activeforeground="lightgreen")
btn9.grid(row=3, column=2,padx=5,pady=5)

btnadd = tkinter.Button(tk, text="+",  command=lambda: add("+"),font=("Time",15),width=5,
                    bg="lightgreen",fg="darkgreen",activebackground="darkgreen",activeforeground="lightgreen")
btnadd.grid(row=3, column=3,padx=5,pady=5)

btn0 = tkinter.Button(tk, text="0",  command=lambda: add("0"),font=("Time",15),width=5,
                    bg="lightgreen",fg="darkgreen",activebackground="darkgreen",activeforeground="lightgreen")
btn0.grid(row=4, column=0,padx=5,pady=5)

btnC = tkinter.Button(tk, text="C",  command=lambda: clean(),font=("Time",15),width=5,
                    bg="lightgreen",fg="darkgreen",activebackground="darkgreen",activeforeground="lightgreen")
btnC.grid(row=4, column=1,padx=5,pady=5)

btnDOT = tkinter.Button(tk, text=".",  command=lambda: add("."),font=("Time",15),width=5,
                    bg="lightgreen",fg="darkgreen",activebackground="darkgreen",activeforeground="lightgreen")
btnDOT.grid(row=4, column=2,padx=5,pady=5)

btnSUB = tkinter.Button(tk, text="-",  command=lambda: add("-"),font=("Time",15),width=5,
                    bg="lightgreen",fg="darkgreen",activebackground="darkgreen",activeforeground="lightgreen")
btnSUB.grid(row=4, column=3,padx=5,pady=5)

btnEQ = tkinter.Button(tk, text="=", width=16,   command=lambda: final_Calc(),font=("Time",15),
                    bg="lightgreen",fg="darkgreen",activebackground="darkgreen",activeforeground="lightgreen")
btnEQ.grid(row=5, column=0, columnspan=4,padx=5,pady=5)

tk.mainloop()