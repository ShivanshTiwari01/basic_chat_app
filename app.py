from tkinter import *
from tkinter import messagebox as ms
from PIL import ImageTk,Image

import server,client

window = Tk()
window.geometry("1000x668")
window.title("Smart Chat")
bg_image = ImageTk.PhotoImage(Image.open("bgphoto.jpg"))
w = Label(window,image=bg_image,justify=CENTER)
w.pack()
window.resizable(0,0)

l_intro = Label(text="Welcome To Smart Chat",fg="dark green",bg="light cyan",font=(25,))
l_intro.place(x=325,y=20,height=75,width=300)

b_server = Button(window,text="Launch Server",fg="black",bg="cyan",command=lambda:[window.destroy(), server.ser_start()])
b_server.place(x=50,y=150,height=60,width=180)

b_login = Button(window,text="Join Chat",fg="black",bg="cyan",command=lambda:[window.destroy(), client.cli_conn()])
b_login.place(x=50,y=250,height=60,width=180)

b_help = Button(window,text="Smart Help",fg="black",bg="cyan",command=lambda: ms.showinfo(title="Message", message="This Feature Coming Soon..."))
b_help.place(x=775,y=550,height=60,width=180)

window.mainloop()
