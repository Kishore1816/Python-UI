from tkinter import *
import tkinter.font as font
import csv
from tkinter import messagebox

root = Tk()

def button_click():
    mail=entry1.get()
    user=entry2.get()
    pwd=entry3.get()
    pwd1=entry4.get()
    if pwd != pwd1:
        messagebox.showerror(title="Sign Up Failed", message="Confirm the right password.")
    else:
        with open('details.csv','a') as f:
            a=csv.writer(f)
            a.writerow([user,pwd])
       
        messagebox.showinfo(title="Sign Up Successful", message="You Have Successfully Signed Up.")
        root.destroy()
        import Returning_user
        
    

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
label1.place(x=width1/2.3, y=height1/5.5)
label2=Label(frame1, text="We're so excited to have you here!", fg='white', bg='#313338', font=('Franklin Gothic Demi', 15))
label2.place(x=width1/2.55, y=height1/4)

label3=Label(frame1, text='Enter your Email id:', fg='white', bg='#313338', font=('Franklin Gothic Demi', 8))
label3.place(x=width1/5, y=height1/3)
label5=Label(frame1, text='*', fg='red', bg='#313338', font=('Franklin Gothic Demi', 8))
label5.place(x=width1/3.7, y=height1/3)
entry1=Entry(frame1, fg='white', bg='#1E1E20', borderwidth=0, width=51, font=('Franklin Gothic Demi', 20))
entry1.place(x=width1/5, y=height1/2.75)

label4=Label(frame1, text='Enter your Username:', fg='white', bg='#313338', font=('Franklin Gothic Demi', 8))
label4.place(x=width1/5, y=height1/2.4)
label6=Label(frame1, text='*', fg='red', bg='#313338', font=('Franklin Gothic Demi', 8))
label6.place(x=width1/3.6, y=height1/2.4)
entry2=Entry(frame1, fg='white', bg='#1E1E20', borderwidth=0, width=51, font=('Franklin Gothic Demi', 20))
entry2.place(x=width1/5, y=height1/2.25)

label7=Label(frame1, text='Enter your Password:', fg='white', bg='#313338', font=('Franklin Gothic Demi', 8))
label7.place(x=width1/5, y=height1/2.01)
label8=Label(frame1, text='*', fg='red', bg='#313338', font=('Franklin Gothic Demi', 8))
label8.place(x=width1/3.6, y=height1/2.02)
entry3=Entry(frame1, fg='white', bg='#1E1E20', borderwidth=0, width=51, font=('Franklin Gothic Demi', 20),show='*')
entry3.place(x=width1/5, y=height1/1.9)

label9=Label(frame1, text='Confirm your Password:', fg='white', bg='#313338', font=('Franklin Gothic Demi', 8))
label9.place(x=width1/5, y=height1/1.73)
label10=Label(frame1, text='*', fg='red', bg='#313338', font=('Franklin Gothic Demi', 8))
label10.place(x=width1/3.5, y=height1/1.73)
entry4=Entry(frame1, fg='white', bg='#1E1E20', borderwidth=0, width=51, font=('Franklin Gothic Demi', 20),show='*')
entry4.place(x=width1/5, y=height1/1.65)

img=PhotoImage(file='Sign_up.png')
button1=Button(frame1, image=img, borderwidth=0, bg='#313338',command=button_click)
button1.place(x=width1/2-150,y=height1/1.5)



root.mainloop()
