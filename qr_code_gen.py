from tkinter import *
import qrcode
master=Tk()
master.title("Url Shortner")
      


def gen():
    link=url.get()
    imag=qrcode.make(link)
    imag.save("qr.jpg")
    img = PhotoImage(file="qr.jpg")      
    canvas.create_image(20,20, anchor=NW, image=img)      
    mainloop()

def delete1():
    url.delete(0,END)

label1=Label(master,text="Welcome To QR Code Generator ",font=("Helvetica",20,"bold"))
label2=Label(master,text="Enter your Url Here :-",font=("roboto",14))
url=Entry(master)
button1=Button(master,text="Generate QR Code",command=gen,padx=20,pady=5)
button2=Button(master,text="Clear",command=delete1,padx=50,pady=5)
button3=Button(master,text="Exit",command=master.quit,padx=58,pady=5)
label4=Label(master,text="Software Designed By Suneet Verma",font=("roboto",8,"italic"))
canvas = Canvas(master, width = 300, height = 300)



label1.grid(row=0,column=0,columnspan=3)
label2.grid(row=1,column=0)
url.grid(row=1,column=1,ipadx=20,ipady=10)
button1.grid(row=2,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=0)
label4.grid(row=5,column=0,columnspan=2)
canvas.grid(row=4,column=0,columnspan=2)

master.mainloop() 