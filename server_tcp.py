import socket

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 12345))
server_socket.listen(5)
print("TCP Server is listening...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    # Chat loop
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        print(f"Client: {message}")
        response = input("You: ")
        client_socket.send(response.encode())

    client_socket.close()

server_socket.close()
