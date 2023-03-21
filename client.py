import socket,threading
from tkinter import *

def cli_conn():

    global msg_list   

    def receive():
    
        global client_socket, msg_list
        while True:
            try:
                msg = client_socket.recv(BUFSIZ).decode("utf8")
                msg_list.insert(END, msg)
            except OSError:  # Possibly client has left the chat.
                break

    def send(event=None):

        global client_socket
        msg = my_msg.get()
        my_msg.set("")  # Clears input field.
        client_socket.send(bytes(msg, "utf8"))
        if msg == "{quit}":
            client_socket.close()

    def on_closing(event=None):
    
        my_msg.set("{quit}")
        send()

    win_cli = Tk()
    win_cli.geometry("600x700")
    win_cli.title("Client")
    win_cli.config(bg="gray8")
    win_cli.resizable(0,0)

    messages_frame = Frame(win_cli)
    messages_frame.place(x=20,y=20,height=540,width=560)
    my_msg = StringVar()
    my_msg.set("")
    chat_screen = Scrollbar(messages_frame)
    chat_screen.pack()
    msg_list = Listbox(messages_frame, yscrollcommand=chat_screen.set, bg="gray10",fg="green4",font=14)
    msg_list.place(x=0,y=0,height=540,width=560)
    entry_field = Entry(win_cli,textvariable=my_msg,bg="gray75",fg="green4",justify=RIGHT,font=14)
    entry_field.bind("<Return>",send)
    entry_field.place(x=20,y=570,height=50,width=560)
    b_send = Button(win_cli,text="Send",fg="black",bg="OrangeRed2",font=(15,),command=send)
    b_send.place(x=20,y=640,height=50,width=560)
    
    HOST = "localhost"
    PORT = 33000
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(ADDR)
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    win_cli.mainloop()
