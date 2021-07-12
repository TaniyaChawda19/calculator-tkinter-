##################################################################calculator#####################################################################################



from tkinter import *
import tkinter.messagebox
root=Tk()

eq=""

equation=StringVar()##StringVar()helps to update label text as value of eq change
calculation=Label(root,textvariable=equation)#text variable is used

calculation.grid(columnspan=4)
equation.set("Enter Your Equation")

def pressbtn(num):
    global eq
    eq=eq+str(num)
    equation.set(eq)

def Clear():
    global eq
    eq=""
    equation.set(eq)

def equal():
    global eq
    data=str(eval(eq))
    equation.set(data)
    eq=""



button1=Button(root,text="  1  ",command=lambda:pressbtn(1))
button1.grid(row=1,column=0)

button2=Button(root,text="  2  ",command=lambda:pressbtn(2))
button2.grid(row=1,column=1)

button3=Button(root,text="  3  ",command=lambda:pressbtn(3))
button3.grid(row=1,column=2)

button4=Button(root,text="  4  ",command=lambda:pressbtn(4))
button4.grid(row=2,column=0)

button5=Button(root,text="  5  ",command=lambda:pressbtn(5))
button5.grid(row=2,column=1)

button6=Button(root,text="  6  ",command=lambda:pressbtn(6))
button6.grid(row=2,column=2)

button7=Button(root,text="  7  ",command=lambda:pressbtn(7))
button7.grid(row=3,column=0)

button8=Button(root,text="  8  ",command=lambda:pressbtn(8))
button8.grid(row=3,column=1)

button9=Button(root,text="  9  ",command=lambda:pressbtn(9))
button9.grid(row=3,column=2)

button0=Button(root,text="  0  ",command=lambda:pressbtn(0))
button0.grid(row=4,column=1)

button11=Button(root,text="  +  ",command=lambda:pressbtn("+"))
button11.grid(row=1,column=3)

button12=Button(root,text="  -  ",command=lambda:pressbtn("-"))
button12.grid(row=2,column=3)

button13=Button(root,text="  *  ",command=lambda:pressbtn("*"))
button13.grid(row=3,column=3)

button14=Button(root,text="  /  ",command=lambda:pressbtn("/"))
button14.grid(row=4,column=3)

button15=Button(root,text="  =  ",command=equal)
button15.grid(row=4,column=2)

button16=Button(root,text="  .  ",command=lambda:pressbtn("."))
button16.grid(row=4,column=0)


clear=Button(root,text="     C    ",command=Clear)
clear.grid(columnspan=4)


tkinter.messagebox.showinfo("Window title","CREATED BY TANIYA CHAWDA")





root.mainloop()

