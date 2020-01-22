from tkinter import *
from tkinter import ttk
import sqlite3
win=Tk()

class Student:
    def __init__(self,win):
        self.win=win
        self.win.title('Student Management System@SaGa Technology')
        self.win.geometry("1350x700+0+0")
        title=Label(self.win,text='Student Management System',bd=10,relief=GROOVE,font=('Times new roman',40,'bold'),bg="cyan",fg="black")
        title.pack(side=TOP,fill=X)
        self.firstname_var=StringVar()
        self.lastname_var = StringVar()
        self.dob_var = StringVar()
        self.contact_var = StringVar()
        self.gender_var = StringVar()
        self.email_var = StringVar()

#manage frame
        manage_frame=Frame(self.win,bd=5,relief=RIDGE,bg="cyan")
        manage_frame.place(x=20,y=100,width=450,height=550)

#manage title
        manage_title=Label(manage_frame,text="Manage Student",bg="cyan",font=('Times new roman',14,'bold'),fg="black")
        manage_title.grid(row=0,columnspan=2,pady=10)

#manage_lable
        #firstname
        manage_lablename=Label(manage_frame,text="First Name :",bg="cyan",font=('Times new roman',14,'bold'),fg="black")
        manage_lablename.grid(row=1,column=0,padx=20,pady=10,sticky='w')

        #lastname
        manage_lablelastname=Label(manage_frame,text='Last Name :',bg='cyan',font=('Times new roman',14,'bold'),fg="black")
        manage_lablelastname.grid(row=2,column=0,padx=20,pady=10,sticky='w')

        #date of birth
        manage_labledob=Label(manage_frame,text='Date of Birth :',bg='cyan',font=('Times new roman',14,'bold'),fg="black")
        manage_labledob.grid(row=3,column=0,padx=20,pady=10,sticky='w')

        #gender
        manage_lablegender=Label(manage_frame,text='Gender :',bg='cyan',font=('Times new roman',14,'bold'),fg="black")
        manage_lablegender.grid(row=4,column=0,padx=20,pady=10,sticky='w')

        #contact num
        manage_lablecontact=Label(manage_frame,text='Contact Number :',bg='cyan',font=('Times new roman',14,'bold'),fg="black")
        manage_lablecontact.grid(row=5,column=0,padx=20,pady=10,sticky='w')

        #email
        manage_lableEmail=Label(manage_frame,text='Email :',bg='cyan',font=('Times new roman',14,'bold'),fg="black")
        manage_lableEmail.grid(row=6,column=0,padx=20,pady=10,sticky='w')

        #Address
        manage_lableaddress=Label(manage_frame,text='Address :',bg='cyan',font=('Times new roman',14,'bold'),fg="black")
        manage_lableaddress.grid(row=7,column=0,padx=20,pady=10,sticky='w')

        #manageEntrybox

        manage_entryfirstname= Entry(manage_frame,textvariable=self.firstname_var,font=('Times new roman',14,'bold'),bd=5,relief=RIDGE)
        manage_entryfirstname.grid(row=1,column=2,padx=20,pady=10,sticky='w')

        manage_entrylastname = Entry(manage_frame,textvariable=self.lastname_var,font=('Times new roman', 14, 'bold'), bd=5, relief=RIDGE)
        manage_entrylastname.grid(row=2,column=2,padx=20,pady=10,sticky='w')

        manage_entrydob = Entry(manage_frame,textvariable=self.dob_var, font=('Times new roman', 14, 'bold'), bd=5, relief=RIDGE)
        manage_entrydob.grid(row=3, column=2, padx=20, pady=10, sticky='w')

        manage_combobox =ttk.Combobox(manage_frame,textvariable=self.gender_var, font=('Times new roman', 14, 'bold'), state='readonly')
        manage_combobox['values']=['Male','Female','Others']
        manage_combobox.grid(row=4, column=2, padx=20, pady=10, sticky='w')

        manage_entrycontact= Entry(manage_frame,textvariable=self.contact_var, font=('Times new roman', 14, 'bold'), bd=5, relief=RIDGE)
        manage_entrycontact.grid(row=5, column=2, padx=20, pady=10, sticky='w')

        manage_entryEmail = Entry(manage_frame,textvariable=self.email_var, font=('Times new roman', 14, 'bold'), bd=5, relief=RIDGE)
        manage_entryEmail.grid(row=6, column=2, padx=20, pady=10, sticky='w')

        self.manage_entryAddress = Text(manage_frame,width=20,height=2.5, font=('Times new roman', 14, 'bold'), bd=5, relief=RIDGE)
        self.manage_entryAddress.grid(row=7, column=2, padx=20, pady=10, sticky='w')

        #buttonframe
        ButtonFrame=Frame(manage_frame,bd=4,bg="cyan",relief=RIDGE)
        ButtonFrame.place(x=5,y=500,width=430)

        addbutton=Button(ButtonFrame,text='ADD',command=self.add_student,width=12)
        addbutton.grid(row=0,column=0,padx=4,pady=3)

        deletebutton = Button(ButtonFrame, text='DELETE',command=self.delete_data,width=12)
        deletebutton.grid(row=0, column=1, padx=4, pady=3)

        updatebutton = Button(ButtonFrame, text='UPDATE',command=self.update_data, width=12)
        updatebutton.grid(row=0, column=2, padx=4, pady=3)

        clearbutton = Button(ButtonFrame, text='CLEAR',command=self.clear_data,width=12)
        clearbutton.grid(row=0, column=3, padx=4, pady=3)

        #show frame
        show_frame=Frame(self.win,bd=5,relief=RIDGE,bg="cyan")
        show_frame.place(x=480,y=100,width=850,height=550)

        show_lablesearch=Label(show_frame,text="Search by :",bg="cyan",font=('Times new roman',14,'bold'),fg="black")
        show_lablesearch.grid(row=0,column=0,padx=20,pady=10,sticky='w')

        show_combobox = ttk.Combobox(show_frame,width=16, font=('Times new roman', 14, 'bold'), state='readonly')
        show_combobox['values'] = ['name', 'email', 'contact']
        show_combobox.grid(row=0, column=1, padx=20, pady=10, sticky='w')

        show_entrysearch = Entry(show_frame, font=('Times new roman', 14, 'bold'), bd=5, relief=RIDGE)
        show_entrysearch.grid(row=0, column=2, padx=20, pady=10, sticky='w')

        searchbutton = Button(show_frame, text='SEARCH', width=12)
        searchbutton.grid(row=0, column=3, padx=4, pady=3,sticky='w')

        showallbutton = Button(show_frame, text='SHOW ALL', width=12)
        showallbutton.grid(row=0, column=4, padx=4, pady=3,sticky='w')

        #table frame
        table_frame=Frame(show_frame,bg="cyan",relief=RIDGE,bd=5)
        table_frame.place(x=10,y=70,height=450,width=760)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=('name','lastname','dob','contact','gender','email','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading('name',text='NAME')
        self.student_table.heading('lastname',text='LASTNAME')
        self.student_table.heading('dob',text='DOB')
        self.student_table.heading('contact',text='CONTACT')
        self.student_table.heading('email',text='EMAIL')
        self.student_table.heading('gender',text='GENDER')
        self.student_table.heading('address',text='ADDRESS')
        self.student_table['show']='headings'
        self.student_table.pack()

        self.student_table.column('name',width=100)
        self.student_table.column('lastname',width=100)
        self.student_table.column('dob',width=100)
        self.student_table.column('contact',width=100)
        self.student_table.column('gender',width=100)
        self.student_table.column('email',width=150)
        self.student_table.column('address',width=150)
        self.student_table.pack(fill='both',expand=1)
        self.student_table.bind('<ButtonRelease-1>',self.get_cursor)
        self.fetch_data()

        # con=sqlite3.connect('student.db')
        # cur=con.cursor()
        # cur.execute('CREATE TABLE student(firstname text,lastname text,contact text,email text,gender text,address text,dob text)')
        # con.commit()
        # con.close()

    def add_student(self):
        con=sqlite3.connect('student.db')
        cur=con.cursor()
        cur.execute('INSERT INTO student values(?,?,?,?,?,?,?)',(self.firstname_var.get(),
                                                                  self.lastname_var.get(),
                                                                  self.dob_var.get(),
                                                                  self.contact_var.get(),
                                                                  self.email_var.get(),
                                                                  self.gender_var.get(),
                                                                  self.manage_entryAddress.get(1.0,END)))
        con.commit()
        self.fetch_data()
        self.clear_data()
        con.close()

    def fetch_data(self):
        con=sqlite3.connect('student.db')
        cur=con.cursor()
        cur.execute('select * from student')
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
            con.close()

    def clear_data(self):
        self.firstname_var.set('')
        self.lastname_var.set('')
        self.contact_var.set('')
        self.email_var.set('')
        self.gender_var.set('')
        self.dob_var.set('')
        self.manage_entryAddress.delete(1.0,END)

    def get_cursor(self,event):
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents['values']
        self.firstname_var.set(row[0])
        self.lastname_var.set(row[1])
        self.gender_var.set(row[2])
        self.contact_var.set(row[3])
        self.email_var.set(row[4])
        self.dob_var.set(row[5])
        self.manage_entryAddress.delete(1.0,END)
        self.manage_entryAddress.insert(END,row[6])

    def update_data(self):
        con=sqlite3.connect('student.db')
        cur=con.cursor()
        cur.execute('update student set firstname=?,lastname=?,gender=?,contact=?,dob=?,email=?,address=?',
                    (
             self.firstname_var.get(),
             self.lastname_var.get(),
             self.dob_var.get(),
             self.contact_var.get(),
             self.email_var.get(),
             self.gender_var.get(),
             self.manage_entryAddress.get(1.0, END)))
        con.commit()
        self.fetch_data()
        self.clear_data()
        con.close()

    def delete_data(self):
        con=sqlite3.connect('student.db')
        cur=con.cursor()
        cur.execute('delete from student where firstname=?',('firstname',))
        con.commit()
        self.fetch_data()
        self.clear_data()
        con.close()

ob=Student(win)
win.mainloop()