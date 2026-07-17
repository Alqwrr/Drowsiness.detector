import socket

HOST = "192.168.4.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Connected!")

while True:
    command = input("Command: ")

    if command.lower() == "exit":
        break

    client.sendall((command + "\n").encode())

client.close()