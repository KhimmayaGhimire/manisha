import tkinter
from tkinter import ttk
from tkinter import messagebox
win=tkinter.Tk()
win.title("messagebox and exception")
win.configure(background="skyblue")
labelframe=tkinter.LabelFrame(win,text="enter your details")
labelframe.grid(row=0,column=0,padx=200,pady=50)

#lable
name_label=ttk.Label(labelframe,text="Enter Your Name ?",font=("Helvetico",14,"bold"))
age_label=ttk.Label(labelframe,text="Enter Your Age ?",font=("Helvetico",14,"bold"))

name_var=tkinter.StringVar()
age_var=tkinter.StringVar()

#entrybox
name_entrybox=ttk.Entry(labelframe,width=50,textvariable=name_var)
age_entrybox=ttk.Entry(labelframe,width=50,textvariable=age_var)

#grid
name_label.grid(row=0,column=0,padx=5,pady=5,sticky=tkinter.W)
age_label.grid(row=0,column=1,padx=5,pady=5,sticky=tkinter.W)
name_entrybox.grid(row=1,column=0,padx=5,pady=5,sticky=tkinter.W)
age_entrybox.grid(row=1,column=1,padx=5,pady=5,sticky=tkinter.W)

def submit():
    name=name_var.get()
    age=age_var.get()
    if age=='' or name=='':
        messagebox.showerror('Error','please enter both details')
    else:
        try:
            age=int(age)
        except ValueError:
            messagebox.showerror('error','please enter interger digit only ')
        else:
            if age<18:
                messagebox.showwarning('warning','you are not above 18, please visit this content on own your risk')
            print(f"{name}:{age}")

button=ttk.Button(win,text='SUBMIT',command=submit)
button.grid(row=1,column=0)

win.mainloop()