import socket

HOST = '127.0.0.1'  # IP-адрес сервера
PORT = 65432        # порт сервера

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Подключен клиент:', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print('От клиента:', data.decode())
            message = input()
            conn.sendall(message.encode())