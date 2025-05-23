import socket

def start_server(host: str, port: int):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server.bind((host, port))
    print(f"server started at {host}:{port}\n Listening now...")

    clients = set()
    
    while True:
        data, addr = server.recvfrom(1024)
        print(f'[CLIENTE]: {data.decode()}')

        if addr not in clients:
            clients.add(addr)

        for client in clients:
            server.sendto(data, client)


if __name__ =='__main__':
   
    HOST =' localhost'
    PORT = 8000

    start_server(HOST, PORT)
