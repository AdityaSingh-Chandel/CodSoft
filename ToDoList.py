from tkinter import *
from tkinter import messagebox

win =Tk()
win.title("To-Do List")
win.geometry('850x450')

win.resizable(False,False)

def add_task():
    task = entry.get()
    if task:
        listbox.insert(END, task)
        entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")



label1=Label(win, text="To-Do List",font=("Algerian",25), fg='red', bg='yellow')
label1.grid(row=0, column=2)

entry= Entry(win,width=20,font=('Lucida',20),borderwidth=6)
entry.grid(row=2,column=1)
entry.focus_set()

button1=Button(win, text="Add Task",font=("Arial Black",18), fg='black', bg='yellow',width=20,command=add_task)
button1.grid(row=3,column=1)

button2=Button(win, text="Remove Task",font=("Arial Black",18), fg='black', bg='yellow',width=20,command=remove_task)
button2.grid(row=3,column=2)

listbox=Listbox(win, width=40,font=('Lucida',15),borderwidth=6)
listbox.grid(column=2,row=2)


win.mainloop()