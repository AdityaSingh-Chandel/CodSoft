from tkinter import *
win =Tk()
#win.geometry('490x325')
win.title("Calculator")

win.resizable(False,False)

SCvalue = StringVar()

a1=''
def click(n):
    global a1
    a1=a1+str(n)
    SCvalue.set(a1)
    
def clear():
    global a1
    a1 = ""
    SCvalue.set("")
    
def equal():
    try:
        global a1
        total=str(eval(a1))
        SCvalue.set(total)
        a1=''
    except:
        SCvalue.set('Error')
        a1=''
        
ent=Entry(win,textvariable=SCvalue,font=('Lucida',25),borderwidth=12,width=15).grid(columnspan=4, ipadx=70)


button1 = Button(win, text=' 1 ',font=('Arial black',12), fg='black', bg='white',command=lambda: click(1), height=3, width=12)
button1.grid(row=2, column=0)

button2 = Button(win, text=' 2 ',font=('Arial black',12), fg='black', bg='white',command=lambda: click(2), height=3, width=12)
button2.grid(row=2, column=1)
 
button3 = Button(win, text=' 3 ',font=('Arial black',12), fg='black', bg='white',command=lambda: click(3), height=3, width=12)
button3.grid(row=2, column=2)
 
button4 = Button(win, text=' 4 ',font=('Arial black',12), fg='black', bg='white',command=lambda: click(4), height=3, width=12)
button4.grid(row=3, column=0)
 
button5 = Button(win, text=' 5 ',font=('Arial black',12), fg='black', bg='white',command=lambda: click(5), height=3, width=12)
button5.grid(row=3, column=1)
 
button6 = Button(win, text=' 6 ',font=('Arial black',12), fg='black', bg='white',command=lambda: click(6), height=3, width=12)
button6.grid(row=3, column=2)
 
button7 = Button(win, text=' 7 ',font=('Arial black',12), fg='black', bg='white',command=lambda: click(7), height=3, width=12)
button7.grid(row=4, column=0)
button8 = Button(win, text=' 8 ',font=('Arial black',12), fg='black', bg='white',command=lambda: click(8), height=3, width=12)
button8.grid(row=4, column=1)
 
button9 = Button(win, text=' 9 ',font=('Arial black',12), fg='black', bg='white',command=lambda: click(9), height=3, width=12)
button9.grid(row=4, column=2)
 
button0 = Button(win, text=' 0 ',font=('Arial black',12), fg='black', bg='white',command=lambda: click(0), height=3, width=12)
button0.grid(row=5, column=0)
 
plus = Button(win, text=' + ',font=('Arial black',12), fg='black', bg='white',command=lambda: click("+"), height=3, width=12)
plus.grid(row=2, column=3)
 
minus = Button(win, text=' - ',font=('Arial black',12), fg='black', bg='white',command=lambda: click("-"), height=3, width=12)
minus.grid(row=3, column=3)
 
multiply = Button(win, text=' * ',font=('Arial black',12), fg='black', bg='white',command=lambda: click("*"), height=3, width=12)
multiply.grid(row=4, column=3)
 
divide = Button(win, text=' / ',font=('Arial black',12), fg='black', bg='white',command=lambda: click("/"), height=3, width=12)
divide.grid(row=5, column=3)

equal = Button(win, text=' = ',font=('Arial black',12), fg='black', bg='white',command=equal, height=3, width=12)
equal.grid(row=5, column=2)
 
clear = Button(win, text='Clear',font=('Arial black',12), fg='black', bg='white',command=clear, height=3, width=12)
clear.grid(row=5, column='1')
 

win.mainloop()