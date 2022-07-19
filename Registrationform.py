import tkinter
from tkinter import *
import tkinter.messagebox
import pymysql


window=Tk()
window.title("profile")
window.geometry("500x500")

a=tkinter.Label(text="Profile creation",bg="indigo",fg="white",font=("Courier", 16, "italic")).place(x=150,y=0)

b=tkinter.Label(text="First name",font=("Courier", 10, "italic")).place(x=50,y=100)
c=tkinter.Entry()
c.place(x=200,y=100)

d=tkinter.Label(text="Location",font=("Courier", 10, "italic")).place(x=50,y=150)
e=tkinter.Entry()
e.place(x=200,y=150)



def abcd():
        name = c.get()
        place = e.get()
        if (name == "" or place == ""):
            tkinter.messagebox.showerror("error", "enter data")
        else:
            x = pymysql.connect(host='localhost', user='root', password='root', db="information")
            cur = x.cursor()
            cur.execute("insert into profile values('" + name + "','" + place + "')")
            x.commit()
            x.close()
            tkinter.messagebox.showinfo("thank you", "thanks for visiting")
            window.destroy()








f=tkinter.Button(text="Submit",font=("Courier", 15, "italic"),bg="indigo",fg="white",command=abcd).place(x=220,y=200)



window.mainloop()
