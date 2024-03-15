import csv
from tkinter import *
from tkinter import messagebox


def button_press():
    user1=entry1.get()
    pwd2=entry2.get()
    list_=[user1,pwd2]
    b=[]
    with open('details.csv','r') as f:
        a=csv.reader(f)
        for i in a:
            b.append(i)    
        if list_ in b:
            messagebox.showinfo(title="Login Successful", message="You Have Successfully Logged In.")
            root.destroy()
            import Main_prog  #add the next file that you want to import (Main prog DNE here)
        else:
            messagebox.showerror(title="Login Failed", message="Invalid ID Or Password.")


root = Tk()

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

frame1=Frame(canvas1,bg = "#313338",width=900, height=600).place(x=width1/2-450,y=height1/2-300)

label1=Label(frame1, text='Welcome,', fg='white', bg='#313338', font=('Franklin Gothic Demi', 30, 'bold'))
label1.place(x=width1/2.3, y=height1/4)
label2=Label(frame1, text="We're so excited to have you here!", fg='white', bg='#313338', font=('Franklin Gothic Demi', 15))
label2.place(x=width1/2.55, y=height1/3)

label3=Label(frame1, text='Enter your Username:', fg='white', bg='#313338', font=('Franklin Gothic Demi', 8))
label3.place(x=width1/5, y=height1/2.35)
label5=Label(frame1, text='*', fg='red', bg='#313338', font=('Franklin Gothic Demi', 8))
label5.place(x=width1/3.55, y=height1/2.35)
entry1=Entry(frame1, fg='white', bg='#1E1E20', borderwidth=0, width=51, font=('Franklin Gothic Demi', 20))
entry1.place(x=width1/5, y=height1/2.2)

label4=Label(frame1, text='Enter your Password:', fg='white', bg='#313338', font=('Franklin Gothic Demi', 8))
label4.place(x=width1/5, y=height1/1.98)
label6=Label(frame1, text='*', fg='red', bg='#313338', font=('Franklin Gothic Demi', 8))
label6.place(x=width1/3.55, y=height1/1.98)
entry2=Entry(frame1, fg='white', bg='#1E1E20', borderwidth=0, width=51, font=('Franklin Gothic Demi', 20),show='*')
entry2.place(x=width1/5, y=height1/1.85)

img=PhotoImage(file='Sign_in.png')
button1=Button(frame1, image=img, borderwidth=0, bg='#313338',command = button_press)
button1.place(x=width1/2-150,y=height1/1.55)


root.mainloop()

