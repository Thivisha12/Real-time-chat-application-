import socket

# Client setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 12345))

print("Connected to the TCP Server...")

# Chat loop
while True:
    message = input("You: ")
    client_socket.send(message.encode())
    if not message:
        break
    response = client_socket.recv(1024).decode()
    if not response:
        break
    print(f"Server: {response}")

client_socket.close()