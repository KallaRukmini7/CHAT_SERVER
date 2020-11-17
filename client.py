import socket

PORT = 1234
FORMAT = "utf-8"
print("ENTER THE SERVER IP: ")
SERVER = input()
DISCONNECT_MESSAGE = "!DISCONNECT"
ADDR = (SERVER, PORT)
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(ADDR)
print("ENTER THE HOSTNAME: ")
h_name=input()
c.send(h_name.encode(FORMAT))
print("ENTER '!DISSCONNECT' TO EXIT ")
s_name=c.recv(1024).decode(FORMAT)
connected=True
print("***** WELCOME TO THE CHAT *****")
while connected:
   msg = input()
   c.send(msg.encode(FORMAT))
   if msg==DISCONNECT_MESSAGE:
    connected=False
   s_msg=c.recv(1024).decode(FORMAT)
   print("Msg from",s_name,"<<",s_msg)

