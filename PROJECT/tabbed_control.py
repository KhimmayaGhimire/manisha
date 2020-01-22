import tkinter
from tkinter import ttk
win=tkinter.Tk()
win.title('TAB widget')
nb=ttk.Notebook(win)
# nb.grid(row=0,column=0)
nb.pack(expand=True,fill='both')
page1=ttk.Frame(nb)
page2=ttk.Frame(nb)

nb.add(page1,text='TAB1')
nb.add(page2,text='TAB2')

page1_label=ttk.Label(page1,text='this tab one')
page1_label.grid(row=0,column=0)

page2_label=ttk.Label(page2,text='this tab two')
page2_label.grid(row=0,column=0)

page1_entry=ttk.Entry(page1)
page1_entry.grid(row=0,column=1)

page2_entry=ttk.Entry(page2)
page2_entry.grid(row=0,column=1)

win.mainloop()