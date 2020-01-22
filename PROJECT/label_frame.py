import tkinter
from tkinter import ttk
win=tkinter.Tk()
win.title("lableframe and padding")
win.configure(background="skyblue")
lableframe=tkinter.LabelFrame(win,text="enter your details")
lableframe.grid(row=0,column=0,padx=500,pady=60)

Lables=['what is your name?',
        'what is your age?',
        'what is your gender?',
        'what is your adress?',
        'country',
        'city']

for i in range(len(Lables)):
    cur_lables='lable'+str(i)
    cur_lables=ttk.Label(lableframe, text=Lables[i])
    cur_lables.grid(row=i,column=0,sticky=tkinter.W)

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
    cur_entrybox=ttk.Entry(lableframe,width=20,textvariable=user_info[i])
    cur_entrybox.grid(row=counter,column=1,padx=10,pady=10)
    counter+=1
def submit():
    print(user_info['name'].get())
    print(user_info.get('age').get())
    print(user_info.get('gender').get())
    print(user_info.get('address').get())
    print(user_info.get('city').get())
    print(user_info.get('coutry').get())

submit_btn=ttk.Button(win,text='submit',command=submit)
submit_btn.grid(row=1,columnspan=2)

win.mainloop()