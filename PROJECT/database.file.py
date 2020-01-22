import sqlite3
conn=sqlite3.connect('test.db')
print("opened database successfully")
# conn.execute("create table student (id int,name text,rollno int,task text)")
# conn.execute("insert into student (id int,name text,rollno int,address text)values(1,manisha,1,butwal)");
conn.commit()
# conn.close()