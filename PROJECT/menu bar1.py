import tkinter
from tkinter import ttk
win=tkinter.Tk()
win.title("menu bar khimmaya")

def function():
    print("this is menu bar")

main_menu=tkinter.Menu(win)

file_menu=tkinter.Menu(main_menu,tearoff=0)
file_menu.add_command(label="new file",command="function")
file_menu.add_separator()
file_menu.add_command(label="save",command="function")

main_menu.add_cascade(menu=file_menu,label="File")

edit_menu=tkinter.Menu(main_menu,tearoff=0)
edit_menu.add_command(label="new file",command="function")

main_menu.add_cascade(menu=edit_menu,label="Edit")
win.configure(menu=main_menu)
win.mainloop()