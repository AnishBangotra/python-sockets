import socket, threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())#Local IPV4 address
# Here socket.gethostname() is your device name
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handel_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode()
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode('utf-8')
            if msg == DISCONNECT_MESSAGE:
                connected = False
                print(f"[{addr}] is disconnected")

            print(f"[{addr}]: {msg}")
            conn.send('Message received'.encode('utf-8'))
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = handel_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")

print("[STARTING] server is starting.......")
start()
