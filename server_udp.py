import socket

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1', 12345))
print("UDP Server is listening...")

while True:
    message, client_address = server_socket.recvfrom(1024)
    message = message.decode()
    print(f"Client ({client_address}): {message}")

    response = input("You: ")
    server_socket.sendto(response.encode(), client_address)