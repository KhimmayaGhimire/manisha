import tkinter
from tkinter import ttk
win=tkinter.Tk()
win.title("widget form using loop")

Lables=['what is your name?',
        'what is your age?',
        'what is your gender?',
        'what is your adress?',
        'country',
        'city']

for i in range(len(Lables)):
    cur_lables='lable'+str(i)
    cur_lables=ttk.Label(win, text=Lables[i])
    cur_lables.grid(row=i,column=0,sticky=tkinter.W,padx=15,pady=15)

#entery box
name_var=tkinter.StringVar()
user_info={
    'name':tkinter.StringVar(),
    'age':tkinter.StringVar(),
    'address':tkinter.StringVar(),
    'gender':tkinter.StringVar(),
    'city':tkinter.StringVar(),
    'coutry':tkinter.StringVar(),
}
counter=0
for i in user_info:
    cur_entrybox='entry'+i
    cur_entrybox=ttk.Entry(win,width=20,textvariable=user_info[i])
    cur_entrybox.grid(row=counter,column=1,padx=15,pady=15)
    counter+=1

def submit():
    print(user_info['name'].get())
    print(user_info.get('age').get())
    print(user_info.get('gender').get())
    print(user_info.get('address').get())
    print(user_info.get('city').get())
    print(user_info.get('coutry').get())

submit_btn=ttk.Button(win,text='submit',command=submit)
submit_btn.grid(row=7,columnspan=2)

win.mainloop()