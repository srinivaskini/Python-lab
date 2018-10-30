import tkinter
import pymysql
import tkinter.messagebox
import tkinter.simpledialog
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
        b1=tkinter.Button(root,text="Update",command=self.update)
        b2=tkinter.Button(root,text="Delete",command=self.delete)
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
    def update(self):
        try:
            query='update student set age=%d,name="%s",branch="%s" where usn="%s"'%(self.age.get(),self.name.get(),self.branch.get(),self.usn.get())
            self.cursor.execute(query)
            self.db.commit()
            tkinter.messagebox.showinfo("Success","Updated succesfully!!")
        except Exception as ex:
            tkinter.messagebox.showerror("Insert error",ex)
    def delete(self):
        try:
            key=tkinter.simpledialog.askstring("Search","Enter usn")
            query='delete from student where usn="%s"'%(key)
            self.cursor.execute(query)
            self.db.commit()
            tkinter.messagebox.showinfo("Deleted","deleted")
        except Exception as ex:
            tkinter.messagebox.showerror("No record found",ex)
            
conn=pymysql.connect('localhost','root','','lab_py')
dbop(conn)
               
             
        
            
        