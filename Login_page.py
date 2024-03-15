from tkinter import *
import tkinter.font as font

root = Tk()
    
def new_user():
    global a
    a=True
    root.destroy()

def returning_user():
    global a
    a=False
    root.destroy()

width1= root.winfo_screenwidth()               
height1= root.winfo_screenheight()

root.geometry("%dx%d" % (width1, height1))
root.state('zoomed')
root.title("Statlyst")
logo = PhotoImage(file="Logo2.png")
root.iconphoto(True, logo)

canvas1 = Canvas(root, width=width1, height=height1)
canvas1.pack(fill='both', expand=True)

bg = PhotoImage(file='BG_Intro_1536.png')
canvas1.create_image(0,0, image=bg, anchor='nw')

canvas1.create_text(170,40, text="STATLYST", font=("Copperplate Gothic Bold", 20), fill="white")

frame1=Frame(canvas1,bg = "#313338",width=500, height=600).place(x=width1/2-250,y=height1/2-300)

label1=Label(frame1, text='Welcome,', fg='white', bg='#313338', font=('Franklin Gothic Demi', 30, 'bold'))
label1.place(x=width1/2.30, y=height1/4)
label2=Label(frame1, text="We're so excited to have you here!", fg='white', bg='#313338', font=('Franklin Gothic Demi', 15))
label2.place(x=width1/2.57, y=height1/3)

r_u= PhotoImage(file='Returning_user1.png')
n_u= PhotoImage(file='New_use1.png')

Button1=Button(frame1, image=n_u, bg='#313338', borderwidth=0, command=new_user)
Button1.place(x=width1/2-150, y=height1/2.4)
Button1=Button(frame1, image=r_u, bg='#313338', borderwidth=0, command=returning_user)
Button1.place(x=width1/2-150, y=height1/1.7)

root.mainloop()

if a==True:
    import New_user
else:
    import Returning_user

