import socket
import time

# Define the host and port
HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 6969

# Create a socket object and bind it to the address and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

# Start listening for incoming connections (max 1 connection at a time)
server_socket.listen(1)
print(f"Listening on {HOST}:{PORT}...")

while True:
    # Accept an incoming connection
    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    # Open a file to write the incoming data
    with open("./received_file", "ab") as f:
        while True:
            # Receive data in chunks
            data = conn.recv(4096)
            if not data:
                break  # End of file
            f.write(data)  # Write received data to the file

    print("File received successfully!")

