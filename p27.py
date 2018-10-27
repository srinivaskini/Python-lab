import tkinter
import pymysql
import tkinter.messagebox
import tkinter.simpledialog
from tensorflow.contrib.framework.python.ops.variables import variable
from idlelib import query
class dbop:
    def __init__(self,db):
        self.db=db
        self.cursor=self.db.cursor()
        root=tkinter.Tk()
        self.usn=tkinter.StringVar()
        self.name=tkinter.StringVar()
        self.age=tkinter.IntVar()
        self.branch=tkinter.StringVar()
        l1=tkinter.Label(root,text='USN')
        e1=tkinter.Entry(root,textvariable=self.usn)
        l2=tkinter.Label(root,text='Name')
        e2=tkinter.Entry(root,textvariable=self.name)
        l3=tkinter.Label(root,text='Age')
        e3=tkinter.Entry(root,textvariable=self.age)
        l4=tkinter.Label(root,text='Branch')
        e4=tkinter.Entry(root,textvariable=self.branch)
        b1=tkinter.Button(root,text="Insert",command=self.insert)
        b2=tkinter.Button(root,text="Search",command=self.search)
        l1.grid(row=0,column=0)
        e1.grid(row=0,column=1)
        l2.grid(row=1,column=0)
        e2.grid(row=1,column=1)
        l3.grid(row=2,column=0)
        e3.grid(row=2,column=1)
        l4.grid(row=3,column=0)
        e4.grid(row=3,column=1)
        b1.grid(row=4,column=0)
        b2.grid(row=4,column=1,sticky="E")
        root.mainloop()
    def insert(self):
        try:
            query='insert into student values("%s","%s",%d,"%s")'%(self.usn.get(),self.name.get(),self.age.get(),self.branch.get())
            self.cursor.execute(query)
            tkinter.messagebox.showinfo("Success","Inserted succesfully!!")
        except Exception as ex:
            tkinter.messagebox.showerror("Insert error",ex)
    def search(self):
        try:
           key=tkinter.simpledialog.askstring("Search","Enter usn")
           q='select * from student where usn="%s"'%(key)
           self.cursor.execute(q)
           if(self.cursor.rowcount==0):
               raise Exception("no record found!!")
           else:
               disp=self.cursor.fetchone()
               str1="Name : "+disp[0]+" USN : "+disp[1]+" Age : "+str(disp[2])+" Branch :"+disp[3]
               tkinter.messagebox.showinfo("Found",str1)
        except Exception as ex:
            tkinter.messagebox.showerror("No record found",ex)
            
conn=pymysql.connect('localhost','root','','lab_py')
dbop(conn)
               
             
        
            
        