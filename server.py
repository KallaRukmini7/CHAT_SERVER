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
    print("ENTER '!DISCONNECT' TO EXIT ")
    print("***** WELCOME TO THE CHAT *****")
    while connected:
        s_msg = input(str('ME >> '))
        if s_msg == DISCONNECT_MESSAGE:
             print( "YOU LEFT THE  CHAT SUCCESSFULLY ")
             conn.send("SERVER IS SUCCESSFULLY DISCONNECTED".encode(FORMAT))
             connected = False
        else:
             conn.send(s_msg.encode(FORMAT))
        msg = conn.recv(1024).decode(FORMAT)
        print("Msg from ",c_name, "<<", msg)
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