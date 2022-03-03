from tkinter import *

root=Tk()

root.geometry("250x250+50+50")
root.title('First Gui')

lblnum1=Label(root,text='First No')
lblnum1.grid(row=0,column=0)

txtnum1=Entry(root)
txtnum1.grid(row=0,column=1)

lblnum2=Label(root,text='Second No')
lblnum2.grid(row=1,column=0)

txtnum2=Entry(root)
txtnum2.grid(row=1,column=1)

btnsum=Button(root,text='Sum Number')
btnsum.grid(row=2,column=0)

btnexit=Button(root,text='Exit')
btnexit.grid(row=2,column=1)

root.mainloop()