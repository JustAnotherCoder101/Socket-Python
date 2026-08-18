import socket
import threading
import time
import pickle


HEADER = 64 
PORT = 5051



SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

clients = {}         
next_id = 1
lock = threading.Lock()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def assign_client_id():
    global next_id
    with lock:
        client_id = next_id
        next_id += 1
    return client_id

def handle_client(conn, addr):
    C_ID = assign_client_id()
    clients[conn] = {"id": C_ID, "username": None}
    print(f"[NEW CONNECTION] {addr} connected, ID: {C_ID}")


    connected = True 
    while connected: 
        
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:

            msg_length = int(msg_length) 
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:  
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    del clients[conn]
    conn.close


        
   
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on the port {PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}" )
        



print("funi sever")
start()


'''
print(f"[LISTENING] Server is listening on the port {PORT}")

while True:
    conn, addr = server.accept()
    print(f"{addr} joined")
    '''