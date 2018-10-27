import tkinter
root=tkinter.Tk()
c=tkinter.Canvas(root,height=500,width=500)
c.pack()
c.create_arc(10,10,490,490,start=0,extent=30,fill="black")
c.create_arc(10,10,490,490,start=90,extent=30,fill="black")
c.create_arc(10,10,490,490,start=180,extent=30,fill="black")
c.create_arc(10,10,490,490,start=270,extent=30,fill="black")
root.mainloop()