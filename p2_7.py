import tkinter
import tkinter.messagebox
import tkinter.simpledialog
import pymysql
def insert():
    sql="insert into employee values(%d,'%s','%s',%d,'%s',%d)"%(ssn.get(),fname.get(),lname.get(),age.get(),place.get(),salary.get())
    try:
        cur.execute(sql)
        tkinter.messagebox.showinfo("Success","Inserted successfully !!!!")
    except Exception as ex:
        tkinter.messagebox.showerror("failure","TRY AGAIN :(")

def delete():
    key=tkinter.simpledialog.askinteger("DELETE","Enter SSN")
    try:
        sql='delete from employee where ssn=%d'%(key)
        #sql="delete from employee where ssn=%d and place='%s'"%(ssn.get(),place.get())
        cur.execute(sql)
        tkinter.messagebox.showinfo("Success","Deleted successfully !!!!")
    except Exception as ex:
        tkinter.messagebox.showerror("failure","TRY AGAIN :(")

def update():
    sql="update employee set fname='%s',lname='%s',age=%d,place='%s',salary=%d where ssn=%d"%(fname.get(),lname.get(),age.get(),place.get(),salary.get(),ssn.get())
    try:
        cur.execute(sql)
        tkinter.messagebox.showinfo("Success","Updated successfully !!!!")
    except Exception as ex:
        tkinter.messagebox.showerror("failure","TRY AGAIN :(")
conn=pymysql.connect("localhost","root","","lab_py")
cur=conn.cursor()
#cur.execute("drop table if exists employee")
cur.execute("create table if not exists employee(ssn int,fname varchar(10),lname varchar(10),age int,place varchar(10),salary int)")
root=tkinter.Tk()
ssn=tkinter.IntVar()
fname=tkinter.StringVar()
lname=tkinter.StringVar()
age=tkinter.IntVar()
place=tkinter.StringVar()
salary=tkinter.IntVar()
l1=tkinter.Label(root,text="SSN")
e1=tkinter.Entry(root,textvariable=ssn)
l2=tkinter.Label(root,text="FNAME")
e2=tkinter.Entry(root,textvariable=fname)
l3=tkinter.Label(root,text="LNAME")
e3=tkinter.Entry(root,textvariable=lname)
l4=tkinter.Label(root,text="AGE")
e4=tkinter.Entry(root,textvariable=age)
l5=tkinter.Label(root,text="PLACE")
e5=tkinter.Entry(root,textvariable=place)
l6=tkinter.Label(root,text="SALARY")
e6=tkinter.Entry(root,textvariable=salary)
b1=tkinter.Button(root,text="Insert",command=insert)
b2=tkinter.Button(root,text="Delete",command=delete)
b3=tkinter.Button(root,text="Update",command=update)
l1.grid(row=0,column=0)
e1.grid(row=0,column=2)
l2.grid(row=1,column=0)
e2.grid(row=1,column=2)
l3.grid(row=2,column=0)
e3.grid(row=2,column=2)
l4.grid(row=3,column=0)
e4.grid(row=3,column=2)
l5.grid(row=4,column=0)
e5.grid(row=4,column=2)
l6.grid(row=5,column=0)
e6.grid(row=5,column=2)
b1.grid(row=6,column=0)
b2.grid(row=6,column=1)
b3.grid(row=6,column=2)
root.mainloop()
