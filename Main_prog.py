from tkinter import *


def analyze1():
    global a
    a=True
    root.destroy()

def compare1():
    global a
    a=False
    root.destroy()

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

frame1=Frame(canvas1,bg = "#313338",width=500, height=600).place(x=width1/2-250,y=height1/2-300)

label1=Label(frame1, text='Welcome User,', fg='white', bg='#313338', font=('Franklin Gothic Demi', 30, 'bold'))
label1.place(x=width1/2.51, y=height1/4)
label2=Label(frame1, text="Whats the mood today!?", fg='white', bg='#313338', font=('Franklin Gothic Demi', 15))
label2.place(x=width1/2.37, y=height1/3)

analyze= PhotoImage(file='Analyse1.png')
compare= PhotoImage(file='Compare1.png')

Button1=Button(frame1, image=analyze, bg='#313338', borderwidth=0, command=analyze1)
Button1.place(x=width1/2-150, y=height1/2.4)
Button1=Button(frame1, image=compare, bg='#313338', borderwidth=0, command=compare1)
Button1.place(x=width1/2-150, y=height1/1.7)


root.mainloop()

if a==True:
    import ticker
else:
    import comparison