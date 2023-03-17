import socket

HOST = '127.0.0.1'  # IP-адрес сервера
PORT = 65432        # порт сервера

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input()
        s.sendall(message.encode())
        data = s.recv(1024)
        print('От сервера: ', data.decode())