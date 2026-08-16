import pickle
import socket
import threading
import pickle

HEADER = 64 
PORT = 5051



SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

running = True
print('''

---------ACTIONS---------
1 - send messaage
2 - disconnect
tba
''')
while running:
    try:

        action = int(input("Pick an option"))
        
    except ValueError:
        action = 0    

    if action == 1:
        print("Input Message:")
        send(input())

    elif action == 2:
        print("Disconect on pressing ENTER:")
        input()
        break

    else:
        print("Pick a valid potion lolz")


send(DISCONNECT_MESSAGE)