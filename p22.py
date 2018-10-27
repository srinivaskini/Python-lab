import tkinter
root=tkinter.Tk()
c=tkinter.Canvas(root,height=250,width=500)
c.pack()
def draw():
    c.delete("all")
    if(shape.get()==1):
        if(color.get()==1):
            c.create_rectangle(10,10,90,50,fill="red")
        else:
            c.create_rectangle(10,10,90,50)
    elif(shape.get()==2):
         if(color.get()==1):
            c.create_oval(10,10,90,50,fill="red")
         else:
            c.create_oval(10,10,90,50)
        
shape=tkinter.IntVar()
color=tkinter.IntVar()
#color.set(2)
r1=tkinter.Radiobutton(root,text="Rectangle",variable=shape,value=1,command=draw)
r2=tkinter.Radiobutton(root,text="Oval",variable=shape,value=2,command=draw)
c1=tkinter.Checkbutton(root,text="Filled",variable=color,onvalue=1,offvalue=2,command=draw)
r1.pack()
r2.pack()
c1.pack()
root.mainloop()
