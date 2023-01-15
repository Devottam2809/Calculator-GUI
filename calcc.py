from tkinter import*

equation=""                         # this will accept the user response as string and then the expression will be evaluated

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)      # after final evaluation the text will appear on thr result label.

def clear():                                # this function clears the result label, each time when button C is pressed on the calculator
    global equation
    equation=""
    label_result.config(text=equation)      # it simply replaces the text with a blank text.

def calculate():                            # this function calculates the expression
    global equation
    result=""
    if equation!="":
        try:
            result=eval(equation)
        except:
            result="Error"
            equation=""
    label_result.config(text=result)        # display of function on result label

root=Tk()                               # create object
root.title("Calculator")                #title of GUI
root.geometry("570x600+100+200")        # size of calculator
root.resizable(0,0)                     # fixed size of calculator
root.configure(bg="#17161b")
root.iconbitmap("favicon.ico")          # adding favicon to GUI

label_result=Label(root,width=25,height=2,text="",font=("arial",30),)       # section where the result will be displayed
label_result.pack()

Button(root,text="c",width=5,height=1,font=("arial",30,"italic"),bd=1,fg="black",bg="green",command=lambda: clear()).place(x=10,y=100)
Button(root,text="/",width=5,height=1,font=("arial",30,"italic"),bd=1,fg="black",bg="white",command=lambda: show("/")).place(x=150,y=100)
Button(root,text="%",width=5,height=1,font=("arial",30,"italic"),bd=1,fg="black",bg="white",command=lambda: show("%")).place(x=290,y=100)
Button(root,text="*",width=5,height=1,font=("arial",30,"italic"),bd=1,fg="black",bg="white",command=lambda: show("*")).place(x=430,y=100)

Button(root,text="7",width=5,height=1,font=("arial",30,"italic"),bd=1,fg="black",bg="white",command=lambda: show("7")).place(x=10,y=200)
Button(root,text="8",width=5,height=1,font=("arial",30,"italic"),bd=1,fg="black",bg="white",command=lambda: show("8")).place(x=150,y=200)
Button(root,text="9",width=5,height=1,font=("arial",30,"italic"),bd=1,fg="black",bg="white",command=lambda: show("9")).place(x=290,y=200)
Button(root,text="-",width=5,height=1,font=("arial",30,"italic"),bd=1,fg="black",bg="white",command=lambda: show("-")).place(x=430,y=200)

Button(root,text="4",width=5,height=1,font=("arial",30,"italic"),bd=1,fg="black",bg="white",command=lambda: show("4")).place(x=10,y=300)
Button(root,text="5",width=5,height=1,font=("arial",30,"italic"),bd=1,fg="black",bg="white",command=lambda: show("5")).place(x=150,y=300)
Button(root,text="6",width=5,height=1,font=("arial",30,"italic"),bd=1,fg="black",bg="white",command=lambda: show("6")).place(x=290,y=300)
Button(root,text="+",width=5,height=1,font=("arial",30,"italic"),bd=1,fg="black",bg="white",command=lambda: show("+")).place(x=430,y=300)

Button(root,text="1",width=5,height=1,font=("arial",30,"italic"),bd=1,fg="black",bg="white",command=lambda: show("1")).place(x=10,y=400)
Button(root,text="2",width=5,height=1,font=("arial",30,"italic"),bd=1,fg="black",bg="white",command=lambda: show("2")).place(x=150,y=400)
Button(root,text="3",width=5,height=1,font=("arial",30,"italic"),bd=1,fg="black",bg="white",command=lambda: show("3")).place(x=290,y=400)
Button(root,text="0",width=11,height=1,font=("arial",30,"italic"),bd=1,fg="black",bg="white",command=lambda: show("0")).place(x=10,y=500)

Button(root,text=".",width=5,height=1,font=("arial",30,"italic"),bd=1,fg="black",bg="white",command=lambda: show(".")).place(x=290,y=500)
Button(root,text="=",width=5,height=3,font=("arial",30,"italic"),bd=1,fg="black",bg="green",command=lambda: calculate()).place(x=430,y=400)

root.mainloop()
