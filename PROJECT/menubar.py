import tkinter
from tkinter import ttk
win=tkinter.Tk()
win.title('Menu Bar-khimmaya')

def fun():
    print('this is menu bar')
# menubar=tkinter.Menu(win)
# menubar.add_command(label='file',command=fun)
# menubar.add_command(label='font',command=fun)
# menubar.add_command(label='view',command=fun)
# menubar.add_command(label='save',command=fun)
# menubar.add_command(label='tools',command=fun)
# menubar.add_command(label='open',command=fun)

main_menu=tkinter.Menu(win)
file_menu=tkinter.Menu(main_menu,tearoff=0)
file_menu.add_command(label='New File       Ctrl+N',command=fun)
file_menu.add_command(label='Open File      Ctrl+O',command=fun)
file_menu.add_separator()
file_menu.add_command(label='Save             Ctrl+S',command=fun)
file_menu.add_command(label='Save As',command=fun)
file_menu.add_separator()
file_menu.add_command(label='Project',command=fun)
file_menu.add_command(label='Exit',command=fun)


#edit file
edit_menu=tkinter.Menu(main_menu,tearoff=0)
edit_menu.add_command(label='Undo           Ctrl+Z',command=fun)
edit_menu.add_separator()
edit_menu.add_command(label='Cut            Ctrl+X',command=fun)
edit_menu.add_command(label='Copy           Ctrl+C',command=fun)
edit_menu.add_command(label='Paste          Ctrl+V',command=fun)
edit_menu.add_command(label='Delete         Del',command=fun)
edit_menu.add_separator()
edit_menu.add_command(label='Find',command=fun)
edit_menu.add_command(label='Select All',command=fun)


#view file
view_menu=tkinter.Menu(main_menu,tearoff=0)
view_menu.add_command(label='Tool windows',command=fun)
view_menu.add_separator()
view_menu.add_command(label='Zoom bar',command=fun)
view_menu.add_command(label='Status Bar',command=fun)
view_menu.add_separator()
view_menu.add_command(label='Active Editor',command=fun)

#code
code_menu=tkinter.Menu(main_menu,tearoff=0)
code_menu.add_command(label='Completion',command=fun)
code_menu.add_command(label='Folding',command=fun)
code_menu.add_separator()
code_menu.add_command(label='Move Line Down',command=fun)
code_menu.add_command(label='Move Line Up',command=fun)
code_menu.add_separator()
code_menu.add_command(label='Inspect Code',command=fun)

#run
run_menu=tkinter.Menu(main_menu,tearoff=0)
run_menu.add_command(label='Run',command=fun)
run_menu.add_command(label='Debug',command=fun)
run_menu.add_separator()
run_menu.add_command(label='Compile',command=fun)
run_menu.add_command(label='Show Code',command=fun)
run_menu.add_separator()
run_menu.add_command(label='Project',command=fun)

#help
help_menu=tkinter.Menu(main_menu,tearoff=0)
help_menu.add_command(label='View Help',command=fun)
help_menu.add_command(label='Find Action',command=fun)
help_menu.add_separator()
help_menu.add_command(label='Documentation',command=fun)
help_menu.add_separator()
help_menu.add_command(label='About',command=fun)

#window
window_menu=tkinter.Menu(main_menu,tearoff=0)
window_menu.add_command(label='Active Tool Window',command=fun)
window_menu.add_command(label='Editor Tabs',command=fun)
window_menu.add_command(label='Notifications',command=fun)
window_menu.add_command(label='Background Tasks',command=fun)

#cascadecode file
main_menu.add_cascade(menu=file_menu,label='File')
main_menu.add_cascade(menu=edit_menu,label='Edit')
main_menu.add_cascade(menu=view_menu,label='View')
main_menu.add_cascade(menu=code_menu,label='Code')
main_menu.add_cascade(menu=run_menu,label='Run')
main_menu.add_cascade(menu=help_menu,label='Help')
main_menu.add_cascade(menu=window_menu,label='Window')

win.configure(menu=main_menu)
win.mainloop()
