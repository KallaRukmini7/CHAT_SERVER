import socket
import threading

HEADER = 64
SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)
PORT = 1234
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE="!DISCONNECT"
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(ADDR)
print("Enter the Host name:")
s_name=input()

def handle_client(conn, addr):
    print(f"[NEW CONNECTIONS] {addr} connected.")
    c_name = conn.recv(1024).decode(FORMAT)
    conn.send(s_name.encode(FORMAT))
    connected=True
    print("***** WELCOME TO THE CHAT *****")
    while connected:
        msg = conn.recv(1024).decode(FORMAT)
        if msg:
         if msg == DISCONNECT_MESSAGE:
             connected=False
             print(c_name ,"<<",msg)
             conn.send("YOU ARE SUCCESSFULLY DISCONNECTED".encode(FORMAT))
         else:
          print("Msg from ",c_name, "<<", msg)
          s_msg=input()
          conn.send(s_msg.encode(FORMAT))
    conn.close()

def start():
    s.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = s.accept()
        thread= threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")
print("[STARTING] server is starting...")
start()