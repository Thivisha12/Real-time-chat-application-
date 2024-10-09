import socket

# Client setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 12345)

print("Connected to the UDP Server...")

# Chat loop
while True:
    message = input("You: ")
    client_socket.sendto(message.encode(), server_address)

    response, server = client_socket.recvfrom(1024)
    response = response.decode()
    print(f"Server: {response}")