from tkinter import *
import tkinter.font as font

root = Tk()

def rootstash():
    root.destroy()
    import Login_page

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
canvas1.create_text(width1/2,250, text="Your Journey Starts Here.", font=('Franklin Gothic Demi', 70, 'bold'), fill='White')
canvas1.create_text(width1/2,320, text="Workspace to connect your mind with the market.", font=('Franklin Gothic Demi', 20), fill='white')

font1 = font.Font(family='Franklin Gothic Demi', size=20)
button1=Button(root, text='Get Started', bg='#373737', fg='white', command=rootstash, padx=100, pady=10,borderwidth=0)
button1['font'] = font1
button1_=canvas1.create_window(width1/2,400, window=button1)

 
root.mainloop()

