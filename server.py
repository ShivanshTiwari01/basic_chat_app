import socket,threading
from tkinter import *

def ser_start():
    
    clients = {}
    addresses = {}
    HOST = "localhost"
    PORT = 33000
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    def accept_incoming_connections():

        while True:
            client, client_address = SERVER.accept()
            print("%s:%s has connected." % client_address)
            client.send(bytes(" **** To start chat, please type your name and press enter **** ", "utf8"))
            addresses[client] = client_address
            threading.Thread(target=handle_client, args=(client,)).start()

    def handle_client(client):

        name = client.recv(BUFSIZ).decode("utf8")
        welcome = 'Welcome %s, If you ever want to quit, type {quit} to exit' % name
        client.send(bytes(welcome, "utf8"))
        msg = "%s has joined the chat!" % name
        broadcast(bytes(msg, "utf8"))
        clients[client] = name
        while True:
            msg = client.recv(BUFSIZ)
            if msg != bytes("{quit}", "utf8"):
                broadcast(msg, name+": ")
            else:
                client.send(bytes("{quit}", "utf8"))
                client.close()
                del clients[client]
                broadcast(bytes("%s has left the chat." % name, "utf8"))
                break

    def broadcast(msg, prefix=""):
        for sock in clients:
            sock.send(bytes(prefix, "utf8")+msg)

    global SERVER
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind(ADDR)
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = threading.Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
