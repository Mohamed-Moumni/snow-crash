import socket
import os
import time

# Configuration
HOST = 'localhost'
PORT = 6969
FILE_PATH = 'received_file'  # Replace with the path to your file

# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    sock.connect((HOST, PORT))

    # Open the file to send
    with open(FILE_PATH, 'rb') as f:
        file_data = f.read()

    # Send the file size first
    file_size = len(file_data)
    sock.sendall(file_size.to_bytes(4, byteorder='big'))

    # Send the file data
    bytes_sent = 0
    start_time = time.time()
    while bytes_sent < file_size:
        chunk = file_data[bytes_sent:bytes_sent + 1024]  # Sending 1KB at a time
        sock.sendall(chunk)
        bytes_sent += len(chunk)
        
        # Check if time has exceeded 30 seconds

    print("File sent successfully.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    time.sleep(20)
    sock.close()
